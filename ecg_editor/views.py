from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

from .models import Report
from .models import Leads
from .models import Parameters
from .models import SourceImage
from .forms import ReportForm
from . import ecg_filters
from json import dumps, loads
import cv2
import base64
import numpy as np
import pickle

cut_path = r'C:\Users\Ekaterina\PycharmProjects\web_editor\ecg_editor\static\ecg_editor\img\2.jpg'
color = 'r'
threshold = 175
delta = 2
resolution = 96
patient_id = 654321
lead_names = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']


def index(request):
    image_src = {}
    with open(cut_path, mode='rb') as file:
        img = file.read()
    image_src['src'] = base64.encodebytes(img).decode('utf-8')
    data = {
        'image': img,
        'width': 1600,
        'height': 742,
    }
    source_image = SourceImage.objects.filter(patient_id=patient_id)
    if len(source_image) == 0:
        source_image = SourceImage()
        source_image.src_image = image_src['src']
        source_image.patient_id = 654321
        source_image.save()
    image_src_json = dumps(image_src)
    return render(request, 'ecg_editor/selection_layout.html', {'data': data,
                                                                'image_src': image_src_json})


def about(request):
    return render(request, 'ecg_editor/about_layout.html')


@csrf_exempt
def cut(request):
    # cv2.imwrite(r"D:\check.jpg", image_i)
    leads = []
    parameters = []
    reports = Report.objects.filter(patient_id=patient_id)
    if len(reports) == 0:
        report = Report()
        for name in lead_names:
            start_x = request.POST[name + '_start_x']
            start_y = request.POST[name + '_start_y']
            end_x = request.POST[name + '_end_x']
            end_y = request.POST[name + '_end_y']
            lead = Leads()
            image = cv2.imread(cut_path)
            lead = createLead(lead, image, start_x, start_y, end_x, end_y, name)
            leads.append(lead)
            parameter = Parameters()
            parameter = updateParameters(parameter, lead)
            parameters.append(parameter)
            parameter.lead = lead
            print('первый лид обработан ' + name)
        report = updateReport(report, leads, parameters)
        report.save()
        for lead in leads:
            lead.report = report
            lead.save()
        for parameter in parameters:
            parameter.save()
    else:
        report = reports[0]
        for name in lead_names:
            start_x = request.POST[name + '_start_x']
            start_y = request.POST[name + '_start_y']
            end_x = request.POST[name + '_end_x']
            end_y = request.POST[name + '_end_y']
            lead = report.leads.filter(name=name)[0]
            image = cv2.imread(cut_path)
            lead = createLead(lead, image, start_x, start_y, end_x, end_y, name)
            lead.save()
            leads.append(lead)
            parameter = lead.parameters
            parameter = updateParameters(parameter, lead)
            parameter.save()
            parameters.append(parameter)
        report = updateReport(report, leads, parameters)
        report.save()

    return HttpResponse(status=200)


@csrf_exempt
def result(request):
    error = ''
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            update_report = Report.objects.filter(patient_id=form.cleaned_data.get("patient_id"))[0]
            update_report.patient_name = form.cleaned_data.get("patient_name")
            update_report.heart_axis = form.cleaned_data.get("heart_axis")
            update_report.conclusion = form.cleaned_data.get("conclusion")
            update_report.additional_info = form.cleaned_data.get("additional_info")
            update_report.date = form.cleaned_data.get("date")
            update_report.is_sinus = form.cleaned_data.get("is_sinus")
            update_report.is_regular = form.cleaned_data.get("is_regular")
            update_report.save()
        else:
            error = 'Неверный ввод'
    if request.method == 'PATCH':
        data = QueryDict(request.body)
        report = Report.objects.filter(patient_id=patient_id)[0]
        leads = []
        parameters = []
        for name in lead_names:
            lead = report.leads.filter(name=name)[0]
            if name == data['name']:
                lead.R = data['json_r']
                lead.Q = data['json_q']
                lead.P = data['json_p']
                lead.S = data['json_s']
                lead.T = data['json_t']
                lead.save()
                parameter = lead.parameters
                parameter = updateParameters(parameter, lead)
                parameter.save()
            leads.append(lead)
            parameter = lead.parameters
            parameters.append(parameter)
        report = updateReport(report, leads, parameters)
        report.save()

    report = Report.objects.filter(patient_id=patient_id)[0]
    # parameter = reports[0].parameters.all()
    # lead = report.leads.all()

    is_sinus = 0
    is_regular = 0
    if report.is_sinus:
        is_sinus = 1
    if report.is_regular:
        is_regular = 1
    data = {
        'patient_id': report.patient_id,
        'patient_name': report.patient_name,
        'heart_axis': report.heart_axis,
        'conclusion': report.conclusion,
        'additional_info': report.additional_info,
        'date': str(report.date),
        'is_sinus': is_sinus,
        'is_regular': is_regular,
    }
    data_json = dumps(data)
    lead_i_json = getLeadJson(report.leads.filter(name='I')[0])
    lead_ii_json = getLeadJson(report.leads.filter(name='II')[0])
    lead_iii_json = getLeadJson(report.leads.filter(name='III')[0])
    lead_avr_json = getLeadJson(report.leads.filter(name='aVR')[0])
    lead_avl_json = getLeadJson(report.leads.filter(name='aVL')[0])
    lead_avf_json = getLeadJson(report.leads.filter(name='aVF')[0])
    lead_v1_json = getLeadJson(report.leads.filter(name='V1')[0])
    lead_v2_json = getLeadJson(report.leads.filter(name='V2')[0])
    lead_v3_json = getLeadJson(report.leads.filter(name='V3')[0])
    lead_v4_json = getLeadJson(report.leads.filter(name='V4')[0])
    lead_v5_json = getLeadJson(report.leads.filter(name='V5')[0])
    lead_v6_json = getLeadJson(report.leads.filter(name='V6')[0])
    # TODO считать высоту с шириной в зависимости от высоты и ширины отведений
    form = ReportForm()
    return render(request, 'ecg_editor/result_layout.html', {'data': data_json,
                                                             'form': form,
                                                             'error': error,
                                                             'lead_i': lead_i_json,
                                                             'lead_ii': lead_ii_json,
                                                             'lead_iii': lead_iii_json,
                                                             'lead_aVR': lead_avr_json,
                                                             'lead_aVL': lead_avl_json,
                                                             'lead_aVF': lead_avf_json,
                                                             'lead_V1': lead_v1_json,
                                                             'lead_V2': lead_v2_json,
                                                             'lead_V3': lead_v3_json,
                                                             'lead_V4': lead_v4_json,
                                                             'lead_V5': lead_v5_json,
                                                             'lead_V6': lead_v6_json})


def settings(request):
    return render(request, 'ecg_editor/settings_layout.html')


def tutorial(request):
    return render(request, 'ecg_editor/tutorial_layout.html')


def updateReport(report, leads, parameters):
    report.patient_id = 654321
    report.patient_name = "Даниил"
    report.is_sinus = True
    report.is_regular = True
    report.heart_axis = "Вертикальное положение электрической оси"
    report.conclusion = "Ab"
    # TODO: заключение норм построить
    report.additional_info = ""
    return report


def updateParameters(parameter, lead):
    # TODO
    parameter.is_P = True
    s = loads(lead.S)
    p = loads(lead.P)
    q = loads(lead.Q)
    r = loads(lead.R)
    t = loads(lead.T)
    parameter.QRS_width = abs(s[0][1] - q[0][1]) * 25.4 / resolution
    parameter.QRS_height = abs(q[0][0] - r[0][0]) * 25.4 / resolution
    parameter.R_R = abs(r[1][1] - r[0][1]) * 25.4 / resolution
    parameter.P_R = parameter.R_R / 3
    print(r[1][1], r[0][1])
    return parameter


def createLead(lead, image, start_x, start_y, end_x, end_y, lead_name):
    image_cut = ecg_filters.cutImage(image, start_x, start_y, end_x, end_y)
    signal = ecg_filters.getPixelsSignal(image_cut, color, delta, threshold)
    R = ecg_filters.selectR(signal)
    Q = ecg_filters.selectQ(signal, R)
    S = ecg_filters.selectS(signal, R)
    # TODO
    P = []
    T = []
    lead.name = lead_name
    lead.P = dumps(P)
    lead.Q = dumps(Q)
    lead.R = dumps(R)
    lead.S = dumps(S)
    lead.T = dumps(T)
    lead.array = dumps(signal)
    return lead


def getLeadJson(lead):
    parameters = lead.parameters
    lead_arr = loads(lead.array)
    height = maxPointValue(lead_arr) + 10
    lead_i_data = {
        'P': lead.P,
        'Q': lead.Q,
        'R': lead.R,
        'S': lead.S,
        'T': lead.T,
        'array': lead.array,
        'is_P': parameters.is_P,
        'QRS_width': parameters.QRS_width,
        'QRS_height': parameters.QRS_height,
        'R_R': parameters.R_R,
        'P_R': parameters.P_R,
        'width': len(lead_arr),
        'height': height
    }
    return dumps(lead_i_data)


def maxPointValue(arr):
    maximum = 0
    for point in arr:
        if maximum < point[0]:
            maximum = point[0]
    return maximum


def minPointValue(arr):
    minimum = arr[0][0]
    for point in arr:
        if minimum > point[0]:
            minimum = point[0]
    return minimum

# import numpy as np
# import base64
# import json
# import pickle
# from PIL import Image

# def im2json(im):
#     """Convert a Numpy array to JSON string"""
# imdata = pickle.dumps(im)
# jstr = json.dumps({"image": base64.b64encode(imdata).decode('ascii')})
# return jstr

# def json2im(jstr):
#    """Convert a JSON string back to a Numpy array"""
# load = json.loads(jstr)
# imdata = base64.b64decode(load['image'])
# im = pickle.loads(imdata)
# return im

# Create solid red image
# red = np.full((480, 640, 3), [0, 0, 255], dtype=np.uint8)

# Make image into JSON string
# jstr = im2json(red)

# Extract image from JSON string, and convert from OpenCV to PIL reversing BGR to RGB on the way
# OpenCVim = json2im(jstr)
# PILimage = Image.fromarray(OpenCVim[...,::-1])
# PILimage.show()
