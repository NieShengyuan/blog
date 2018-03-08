# _*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/3/7 
# time   :11:03

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
