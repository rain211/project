#coding=utf-8
from django.conf.urls import url

from library import views

urlpatterns = [
    url(r'^login/',views.login_view),
    url(r'^main/', views.main_view),
    url(r'^library_modify/', views.library_modify_view),
]