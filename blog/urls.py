from django.urls import path
from . import views

urlpatterns = [
    #나중에 채울 겁니다!!
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()), #추가
    # path('',views.index),
]