#coding=utf-8
from django.conf.urls import url

from library import views

urlpatterns = [
    url(r'^login/',views.login_view),
]