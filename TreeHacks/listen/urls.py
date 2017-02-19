from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^make-playlist/$', views.make_playlist, name='make_playlist'),
]