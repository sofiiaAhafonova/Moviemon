from django.urls import re_path

from moviemon import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^worldmap/$', views.worldmap, name='worldmap'),
    re_path(r'^battle/<moviemon_id>/$', views.battle, name='battle' ),
    re_path(r'^moviedex/$', views.moviedex, name='moviedex'),
    re_path(r'^moviedex/<moviemon_id>/$', views.details, name='details'),
    re_path(r'^options/$', views.options, name='options'),
    re_path(r'^options/save_game/$', views.save_game, name='save_game'),
    re_path(r'^options/load_game/$', views.load_game, name='load_game'),
]
