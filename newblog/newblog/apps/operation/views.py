from django.shortcuts import render
from django.views import View
from  django.http import JsonResponse
from operation.models import Like,LikeNum,Hous,Comment
from blog.models import Blog
from user.models import UserProfile
from operation.forms import CommentForm

# Create your views here.


#Ajax返回错误信息
def Error(code,massage):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['massage'] = massage
    return  JsonResponse(data)


#Ajax返回成功信息
def Success(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return  JsonResponse(data)


#Ajax返回收藏成功信息
def SuccessHous(massage):
    data = {}
    data['status'] = 'SUCCESS'
    data['massage'] = massage
    return  JsonResponse(data)




#用户点赞
class LikeView(View):
    def post(self,request):
        #判断是否登录
        user = request.user
        if not user.is_authenticated:
            return Error(400,'登录才可点赞哦~~')

        #获取博客的ID
        blog_id = request.POST.get('blog_id','')
        try:
            #获取博客
            blog_like = Blog.objects.get(id=blog_id)
        except:
            return Error(401,'不存在此博客')

        #判断是否点赞
        if request.POST.get('is_like')  == 'true':
            like_record,create = Like.objects.get_or_create(user=user,like_blog=blog_like)
            if create:
                #未点赞过，进行点赞
                like_count,create = LikeNum.objects.get_or_create(like_blog=blog_like)
                like_count.like_num += 1
                like_count.save()
                return Success(like_count.like_num)

            else:
                # 已点赞过，不能重复点赞
                return Error(402, 'you were liked')

        #取消点赞
        else:
            if Like.objects.filter(like_blog=blog_like,user=user):
                #有点赞过，取消点赞
                like_record = Like.objects.get(like_blog=blog_like,user=user).delete()
                #总数减一
                like_count, create = LikeNum.objects.get_or_create(like_blog=blog_like)
                if not create:
                    like_count.like_num -= 1
                    like_count.save()
                    return Success(like_count.like_num)
                else:
                    return Error(404, 'data error')
            else:
                # 没有点赞过，不能取消
                return Error(403, 'you were not liked')




#用户收藏
class HouseView(View):
    def post(self,request):
        #判断是否登录
        user = request.user
        if not user.is_authenticated:
            return Error(400,'登录才可点赞哦~~')

        blog_id = request.POST.get("blog_id","")
        try:
            hous_blog = Blog.objects.get(id=int(blog_id))
        except:
            return Error(401,"没有此博客")

        #未需要收藏
        if request.POST.get("is_hous") == "true":
            user_hous,create = Hous.objects.get_or_create(user=user,fav_blog=hous_blog)
            if not create:
                return Error(402,"已经收藏了")
            return SuccessHous("收藏成功")


        #已收藏，取消收藏
        else:
            if Hous.objects.filter(user=user,fav_blog=hous_blog):
                Hous.objects.get(user=user,fav_blog=hous_blog).delete()
                return SuccessHous("取消收藏成功")

            else:
                return Error(401, "没有此博客")




class CommentView(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return Error(401,"未登录")

        blog_id = int(request.POST.get('blog_id','0'))
        comment = request.POST.get("comment",'')

        try:
            comment_blog = Blog.objects.get(id=blog_id)
        except:
            return Error(404,"没有此博客")

        if comment == '':
            return Error(402,'评论不能为空')


        add_comment = Comment()
        add_comment.user = user
        add_comment.comment_blog = comment_blog
        add_comment.comment = comment
        add_comment.save()

        return SuccessHous("评论成功")






class AddcommentView(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return Error(401, '登录才可评论~~')

        user_id = int(request.POST.get('user_id',0))
        root_id = int(request.POST.get('root_id',0))
        par_id = int(request.POST.get('par_id',0))
        blog_id = int(request.POST.get('blog_id', 0))
        comment = request.POST.get('comment','')

        try:
            root = Comment.objects.get(id=root_id)
            par_id = Comment.objects.get(id=par_id)
            user_id = UserProfile.objects.get(id=user_id)
            blog_id = Blog.objects.get(id=blog_id)
        except:
            return Error(402,"信息错误，无法评论")


        if comment == '':
            return Error(403,"评论不能为空")

        add_rep = Comment()
        add_rep.comment = comment
        add_rep.user = user
        add_rep.comment_blog =blog_id
        add_rep.root = root
        add_rep.parent = par_id
        add_rep.reply_to = user_id
        add_rep.save()

        return SuccessHous("评论成功")
















