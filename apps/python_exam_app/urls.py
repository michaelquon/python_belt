from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^add$', views.add),
    url(r'^addes$', views.add),
    url(r'^create$', views.create),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
]