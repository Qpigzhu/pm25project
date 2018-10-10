# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\10\9 0009 17:03$'

from django import forms

class Pm25_Form(forms.Form):
    city = forms.CharField(required=True)

