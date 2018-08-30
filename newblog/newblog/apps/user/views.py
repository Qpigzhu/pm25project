from django.shortcuts import render,redirect,reverse
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.hashers import make_password
# Create your views here.
from blog.models import BlogType
from .forms import LoginForm,ReForm,ForgetCode,ForgetPwds
from .models import UserProfile,EmailRecord
from .send_email import send_email


#重载登录函数，使得可以用邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


#登录
class LoginView(View):
    def get(self,request):
        all_blog_type = BlogType.objects.all()
        #获取从哪个页面点进来
        froms = request.GET.get('from','')
        return render(request,'login.html',{
            'all_blog_type': all_blog_type,
            'froms':froms
        })

    def post(self,request):
        #生成表单
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username','')
            pwd = request.POST.get('password','')

            user =authenticate(username=username,password = pwd)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.POST.get('next',reverse('home')))
                else:
                    return render(request,'login.html',{"msg":"用户未激活"})
            else:
                return render(request,'login.html',{"msg":"密码或用户错误"})
        else:
            return render(request,'login.html',{
                'login_form':login_form
            })


#注销
class LoginOut(View):
    def get(self,request):

        logout(request)
        return redirect('home')


#注册
class RegisterView(View):
    def get(self,request):
        all_blog_type = BlogType.objects.all()
        return render(request,'register.html',{
            'all_blog_type': all_blog_type,
        })

    def post(self,request):
        re_form = ReForm(request.POST)
        if re_form.is_valid():
            email = request.POST.get('email','')
            username = request.POST.get('username','')
            pwd = request.POST.get('password','')

            if UserProfile.objects.filter(email=email):
                return render(request,'register.html',{'msg':"邮箱已被注册"})
            elif UserProfile.objects.filter(username=username):
                return render(request,'register.html',{'msg':"用户名已被注册"})

            add_user = UserProfile()
            add_user.email = email
            add_user.username = username
            add_user.password = make_password(pwd)
            add_user.is_active = False
            add_user.save()
            send_email(email)
            return render(request,'login.html',{'msg':"邮件已经发送,请激活"})


        else:
            return render(request,'register.html',{
                're_form':re_form
            })


#注册激活
class ReActiveView(View):
    def get(self,request,active_code):
        all_code = EmailRecord.objects.filter(code=active_code)
        if all_code:
            for code in all_code:
                email = code.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                EmailRecord.objects.get(email=email,send_type='register').delete()
                return redirect(reverse('login'))
        else:
            return render(request,'register.html',{'msg':'链接失效'})


#发送重置密码链接
class SendForgetPwd(View):
    def get(self,request):
        forget_code = ForgetCode()
        return render(request,'forget.html',{
            'forget_code':forget_code,
        })

    def post(self,request):
        forget_code = ForgetCode(request.POST)
        if forget_code.is_valid():
            email = request.POST.get('email','')
            if UserProfile.objects.filter(email=email):
                send_email(email,'forget')
                return render(request,'msg.html',{
                    'msg':'邮箱已发送成功',

                })
            else:
                return render(request,'forget.html',{
                    'msg':'不存在此用户',
                    'forget_code':forget_code
                })
        else:
            return render(request,'forget.html',{
                'forget_code': forget_code
            })


#获取重密码页面
class ForgetPwdHtml(View):
    def get(self,request,pwd_code):
        all_pwd_code = EmailRecord.objects.filter(code=pwd_code,send_type='forget')
        if all_pwd_code:
            for code in all_pwd_code:
                email = UserProfile.objects.get(email=code.email)

        else:
            return render(request,'msg.html',{"msg":"链接已失效"})
        return render(request,'forget_pwd.html',{
            'email':email,

        })

#忘记密码处理
class ForgetPwd(View):
    def post(self,request):
        forget_pwd = ForgetPwds(request.POST)
        if forget_pwd.is_valid():
            pwd = forget_pwd.cleaned_data['password1']
            email = request.POST.get('email','')
            user = UserProfile.objects.get(username=email)
            user.password = make_password(pwd)
            user.save()
            EmailRecord.objects.get(email = user.email,send_type='forget').delete()
            return redirect(reverse('login'))

        else:
            return render(request,'msg.html',{
                'msg':'密码不一致'
            })