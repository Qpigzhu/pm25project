from django.contrib import admin
from .models import pm25
# Register your models here.
@admin.register(pm25)
class pm25Admin(admin.ModelAdmin):
    list_display = ('id','city_name','pm25_value','adive','step')
