from django.db import models

from blog.models import Blog
from user.models import UserProfile
# Create your models here.

class LikeNum(models.Model):
    like_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="点赞的博客")
    like_num = models.IntegerField(default=0,verbose_name="点赞数量")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "点赞数量"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.like_blog, self.like_num)


class Like(models.Model):
    like_blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name="点赞的博客")
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="点赞的用户")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "点赞信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.user,self.like_blog)


class Hous(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    fav_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "收藏信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.user,self.fav_blog)


class Comment(models.Model):
    comment_blog = models.ForeignKey(Blog,related_name='comment_blog',on_delete=models.CASCADE,verbose_name="评论的博客")
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="评论的用户")
    comment = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")

    root = models.ForeignKey('self', related_name='root_comment', null=True, blank=True,on_delete=models.CASCADE,verbose_name="顶级的评论")
    parent = models.ForeignKey('self', related_name='parent_comment', null=True,blank=True, on_delete=models.CASCADE,verbose_name="上一级回复的评论")
    reply_to = models.ForeignKey(UserProfile, related_name='replies', null=True, blank=True,on_delete=models.CASCADE,verbose_name="回复用户")


    def __str__(self):
        return self.comment


    class Meta:
        ordering = ['-add_time']