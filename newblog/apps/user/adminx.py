# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\4 0004 23:31$'

import xadmin
from xadmin import views
from .models import EmailRecord

class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "Pig博客管理"
    site_footer = "Pig博客"
    #收起菜单
    menu_style = "accordion"

class EmailRecordAdmin(object):
    list_dispaly = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type']


xadmin.site.register(EmailRecord,EmailRecordAdmin)


# 将开启主题功能注册
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView,GlobalSettings)