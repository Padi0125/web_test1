from django.urls import path
from . import views

urlpatterns = [
    # 나중에 채울 겁니다!!
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]