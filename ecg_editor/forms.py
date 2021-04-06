from .models import Report
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, Textarea


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['patient_id', 'patient_name', 'date', 'is_sinus', 'is_regular', 'heart_axis', 'conclusion', 'additional_info']
        widgets = {
            "patient_id": TextInput(attrs={
                'class': 'form-control',
                'id': 'inputId',
            }),
            "patient_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов Иван Иванович',
                'id': 'inputName',
                # 'value': "{{ reports.patient_id }}"
            }),
            "date": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'inputDate',
                # 'value': "{{ date }}"
            }),
            "is_sinus": CheckboxInput(attrs={
                'id': 'is_sinus',
                'class': 'form-check-input',
                'value': "sinus",
                'name': "checkboxes_e"
            }),
            "is_regular": CheckboxInput(attrs={
                'id': 'is_regular',
                'class': 'form-check-input',
                'value': "regular",
                'name': "checkboxes_e"
                # 'value': "{{ reports.patient_id }}"
            }),
            "heart_axis": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите положение электрической оси сердца...',
                'id': 'inputAxis',
                # 'value': "{{ reports.patient_id }}"
            }),
            "conclusion": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Заключение...',
                'id': 'inputReport',
                'rows': '3',
                # 'value': "{{ reports.patient_id }}"
            }),
            "additional_info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введие дополнительную информацию...',
                'id': 'inputAdd',
                'rows': '3',
                # 'value': "{{ reports.patient_id }}"
            }),
        }
