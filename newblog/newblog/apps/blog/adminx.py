# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\4 0004 23:31$'

import xadmin
from .models import Blog,BlogType

class BlogTypeAdmin(object):
    list_dispaly = ['type_name','add_time']
    search_fields = ['type_name']
    list_filter =['type_name','add_time']


class BlogAdmin(object):

    list_dispaly = ['title','type_name','authon','comment','images','create_time']
    search_fields = ['title','type_name','authon','comment','images']
    list_filter =['title','type_name','authon','comment','images','create_time']
    style_fields = {"comment": "ueditor"}

xadmin.site.register(Blog,BlogAdmin)
xadmin.site.register(BlogType,BlogTypeAdmin)
