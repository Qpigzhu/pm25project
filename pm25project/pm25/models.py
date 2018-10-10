from django.db import models

# Create your models here.

class pm25(models.Model):
    city_name = models.CharField(max_length=20,verbose_name="城市名")
    pm25_value = models.IntegerField(default=0,verbose_name="PM25值")
    adive = models.TextField(verbose_name="建议")
    step = models.TextField(verbose_name="措施")
    grade = models.TextField(verbose_name="等级",null=True,blank=True)