from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),   
]
#blog관련 url은 blog앱 안에서 처리하겠다.