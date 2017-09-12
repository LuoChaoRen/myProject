from django.conf.urls import include,url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^list$', views.list, name="list"), 
    url(r'^xiangq$', views.xiangq, name="xiangq"), 
    url(r'^dengl$', views.dengl, name="dengl"), 
    url(r'^gouw$', views.gouw, name="gouw"), 
]