from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views



urlpatterns = [
    # path('upload/', views.ImageUploadView.as_view()),
    path('admin/', views.AdminPostingList.as_view()),
    path('<int:pk>/', views.PostingDetail.as_view()),
    path('', views.UserPostingList.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
