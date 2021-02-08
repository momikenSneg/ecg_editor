from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#   return HttpResponse("<h3>Hello world!</h3>")

def index(request):
    data = {
        'image': r'D:\2.jpg',
        'width': 1600,
        'height': 742,
    }


    return render(request, 'ecg_editor/selection_layout.html', data)


def about(request):
    return render(request, 'ecg_editor/about_layout.html')


def result(request):
    return render(request, 'ecg_editor/result_layout.html')


def settings(request):
    return render(request, 'ecg_editor/settings_layout.html')


def tutorial(request):
    return render(request, 'ecg_editor/tutorial_layout.html')

