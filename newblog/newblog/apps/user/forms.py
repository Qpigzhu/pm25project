# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\6 0006 21:29$'

from django  import forms
from captcha.fields import CaptchaField

#登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


#注册
class ReForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)
    email = forms.EmailField(required=True)

#重置密码
class ForgetCode(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

class ForgetPwds(forms.Form):
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("密码不一致")
        else:
            return password1