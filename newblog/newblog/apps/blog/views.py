from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger   #分页第三库
from .models import Blog,BlogType
from operation.models import Like,LikeNum,Hous,Comment

class BlogListView(View):
    def get(self,request):
        all_blogs = Blog.objects.all()
        all_blog_type = BlogType.objects.all()

        #分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_blogs,5,request=request)

        all_blog = p.page(page)


        return render(request,'index.html',{
            'all_blog':all_blog,
            'all_blog_type':all_blog_type,
        })


class BlogDatil(View):
    def get(self,request,blog_id):
        blogs = Blog.objects.get(id = int(blog_id))


        #判断是否点赞
            #判断是否登录
        if request.user.is_authenticated:
            like_chang = Like.objects.filter(like_blog=blogs,user=request.user)
            if like_chang:
                active_like = 'true_like'
            else:
                active_like = 'false_like'
        else:
            active_like = 'false_like'

        #获取点赞数
        try:
            like_num = LikeNum.objects.get(like_blog=blogs).like_num
        except:
            like_num = 0


        #判断是否已经收藏
        if request.user.is_authenticated:
            hous_chang = Hous.objects.filter(user=request.user,fav_blog=blogs)
            if hous_chang:
                active_hous = 'true_like'
                hous_status = '已收藏'
            else:
                active_hous = 'false_like'
                hous_status = '未收藏'
        else:
            active_hous = 'false_like'
            hous_status = '未收藏'


        #获取评论
        all_comment = Comment.objects.filter(comment_blog=blogs,root=None)


        all_blog_type = BlogType.objects.all()
        return render(request,'blogdatli.html',{
            'blog_datil':blogs,
            'all_blog_type':all_blog_type,
            'active_like':active_like,
            'like_num':like_num,
            'active_hous':active_hous,
            'hous_status':hous_status,
            'all_comment':all_comment
        })


class BlogTypeView(View):
    def get(self,request,type_id):
        blog_type = BlogType.objects.get(id=int(type_id))
        all_blog_type = BlogType.objects.all()
        all_blogs = Blog.objects.filter(type_name=blog_type)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

            # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_blogs, 5, request=request)

        blogs= p.page(page)


        return render(request,'blogtype.html',{
            'Type':blog_type,
            'blogs_list':blogs,
            'all_blog_type': all_blog_type,


        })

