from django.urls import path

from . import views

urlpatterns = [

    path('', views.writings, name='writings'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
