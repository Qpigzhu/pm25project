# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\9 0009 21:26$'


from django.urls import path,re_path
from .views import LikeView,HouseView,CommentView,AddcommentView

urlpatterns = [
    #处理点赞
    path('like/',LikeView.as_view(),name="like"),
    path('hous/',HouseView.as_view(),name='hous'),
    path('comment/',CommentView.as_view(),name='comment'),
    path('add_comment/',AddcommentView.as_view(),name='rep')

]