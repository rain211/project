from django.conf.urls import url
from reader import views
urlpatterns = [
    url(r'^readerset',views.readerset_view),
    url(r'^readertype',views.readertype_view),
]
