# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\6 0006 13:49$'


from django.urls import path,re_path
from .views import BlogTypeView,BlogDatil

urlpatterns = [
    #Blog的类型
    path('type/<int:type_id>',BlogTypeView.as_view(),name="blog_type"),
    #Blog的详情
    path('<int:blog_id>',BlogDatil.as_view(),name = "blog_datil"),

]
