# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\8\13 0013 13:44$'

from django  import forms


class CommentForm(forms.Form):
    blog_id = forms.CharField(required=True)
    comment = forms.Textarea()