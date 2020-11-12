from django.contrib import admin
from django.urls import path,include,re_path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import home,param,regular_param,create_developer

urlpatterns = [
    path('',home),
    path(r'param/<int:pk>',param),
    re_path(r'regular/(?P<pk>\d+)$',regular_param),
    re_path(r'create-developer$',create_developer,name="create_developer")
]
