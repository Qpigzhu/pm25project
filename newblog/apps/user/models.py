from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nice_name = models.CharField(max_length=20,verbose_name="昵称")
    image = models.ImageField(upload_to="user/%Y%m",default="user/default.jpg",verbose_name="头像")
    gender = models.CharField(choices=(("nan","男"),("nv","女")),max_length=10,default="nan",verbose_name="性别")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

class EmailRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(verbose_name="邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型",choices=(("register",u"注册"),("forget",u"忘记密码")),max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", auto_now_add=True)

    class Meta:
        verbose_name = u"邮箱验证"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{}:{}".format(self.email,self.code)