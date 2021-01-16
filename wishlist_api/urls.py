from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^private_wish/(?P<pk>[0-9]+)$', views.private_wish_view),
    url(r'^public_wish/(?P<pk>[0-9]+)$', views.public_wish_view),
    url(r'^access_level/', views.access_uuid_generator)
]