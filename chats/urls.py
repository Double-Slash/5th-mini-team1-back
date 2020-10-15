from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views



urlpatterns = [
    path('from/', views.SpecificChatList.as_view()),
    # path('<int:pk>/', views.ChatDetail.as_view()),
    path('', views.AllChatList.as_view()),
]

