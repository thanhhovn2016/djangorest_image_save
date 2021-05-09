from django.conf.urls import url
from djr import views

urlpatterns = [
    url(r'^djr/$', views.snippet_list),
    url(r'^djr/(?P<pk>[0-9]+)/$', views.snippet_detail),
]