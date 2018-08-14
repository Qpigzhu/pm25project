# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\5 0005 0:08$'


import xadmin
from .models import LikeNum,Like,Hous,Comment

class LikeNumAdmin(object):
    list_dispaly = ['like_blog', 'like_num','add_time']
    search_fields = ['like_blog', 'like_num']
    list_filter = ['like_blog', 'like_num','add_time']


class LikeAdmin(object):
    list_dispaly = ['like_blog', 'user','add_time']
    search_fields = ['like_blog', 'user']
    list_filter = ['like_blog', 'user','add_time']

class HousAdmin(object):
    list_dispaly = ['user', 'fav_blog','add_time']
    search_fields = ['user','fav_blog']
    list_filter = ['user', 'fav_blog','add_time']


class CommentAdmin(object):
    list_dispaly = ['comment_blog', 'user','comment','add_time','root','parent','reply_to']
    search_fields = ['comment_blog', 'user','comment','root','parent','reply_to']
    list_filter = ['comment_blog', 'user','comment','add_time','root','parent','reply_to']



xadmin.site.register(Like,LikeAdmin)
xadmin.site.register(LikeNum,LikeNumAdmin)
xadmin.site.register(Hous,HousAdmin)
xadmin.site.register(Comment,CommentAdmin)