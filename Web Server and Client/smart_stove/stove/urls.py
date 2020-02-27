from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getstate/', views.getState, name='state'),
    path('mobileApp/', views.mobileApp, name='mobile'),
    path('savestate/<str:temp>/<str:p1>/<str:p2>', csrf_exempt(views.saveState), name='save'),
]
