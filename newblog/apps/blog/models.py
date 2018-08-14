from django.db import models
from user.models import UserProfile
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=20,verbose_name="标签")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    type_name = models.ForeignKey(BlogType,on_delete=models.CASCADE,verbose_name="标签")
    authon = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="作者")
    comment = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name = "创建时间")
    images = models.ImageField(upload_to="blog/%Y/%m",verbose_name="封面")

    class Meta:
        verbose_name = "博客"
        verbose_name_plural =verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title

