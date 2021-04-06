from django.conf import settings
from django.db import models
from django.utils import timezone


class SourceImage(models.Model):
    patient_id = models.BigIntegerField()
    src_image = models.ImageField()

    class Meta:
        verbose_name = 'SourceImage'
        verbose_name_plural = 'SourceImages'


class Report(models.Model):
    patient_id = models.BigIntegerField()
    patient_name = models.CharField(max_length=128)
    date = models.DateField(default=timezone.now)
    is_sinus = models.BooleanField()
    is_regular = models.BooleanField()
    heart_axis = models.CharField(max_length=256)
    conclusion = models.CharField(max_length=512)
    additional_info = models.CharField(max_length=512)

    def __str__(self):
        return 'report'

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


class Leads(models.Model):
    report = models.ForeignKey(Report, related_name="leads", on_delete=models.CASCADE)
    name = models.CharField(max_length=3)
    P = models.JSONField()
    Q = models.JSONField()
    R = models.JSONField()
    S = models.JSONField()
    T = models.JSONField()
    array = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Leads'
        verbose_name_plural = 'Leads'


class Parameters(models.Model):
    lead = models.OneToOneField(Leads, related_name="parameters", on_delete=models.CASCADE, primary_key=True,)
    is_P = models.BooleanField()
    QRS_width = models.FloatField()
    QRS_height = models.FloatField()
    R_R = models.FloatField()
    P_R = models.FloatField()

    def __str__(self):
        return 'param'

    class Meta:
        verbose_name = 'Parameters'
        verbose_name_plural = 'Parameters'
