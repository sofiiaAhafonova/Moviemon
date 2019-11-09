from django.urls import re_path

from moviemon import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^worldmap/$', views.worldmap, name='worldmap'),
]
