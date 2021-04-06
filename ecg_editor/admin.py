from django.contrib import admin
from .models import SourceImage
from .models import Report
from .models import Leads
from .models import Parameters

admin.site.register(SourceImage)
admin.site.register(Report)
admin.site.register(Leads)
admin.site.register(Parameters)

# Register your models here.
