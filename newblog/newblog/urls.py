"""newblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve

from .settings import MEDIA_ROOT
from blog.views import BlogListView
from user.views import LoginView,LoginOut,RegisterView,ReActiveView,SendForgetPwd,ForgetPwdHtml,ForgetPwd

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    #首页
    path('',BlogListView.as_view(),name="home"),
    #登录
    path('login/',LoginView.as_view(),name="login"),
    #注销
    path('outlogin/',LoginOut.as_view(),name='login_out'),
    #注册
    path('re/',RegisterView.as_view(),name='re_user'),
    #激活
    re_path('active/(?P<active_code>.*)/',ReActiveView.as_view(),name="re_active"),
    #BlogURL
    path('blog/',include('blog.urls')),

    #验证码
    path('captcha/', include('captcha.urls')),

    #发送重置密码邮件
    path('sendcode/',SendForgetPwd.as_view(),name = 'send_forget_pwd'),
    #返回重置密码页面
    re_path('forget/(?P<pwd_code>.*)/',ForgetPwdHtml.as_view(),name='forget_pwd_html'),
    #处理重置密码
    path('forgetpwd/',ForgetPwd.as_view(),name='forget_pwd'),

    #用户操作
    path('operation/',include('operation.urls'))
]
