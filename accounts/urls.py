from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from accounts import views
# from rest_framework.authtoken.views import ObtainAuthToken


router = SimpleRouter()
router.register(r'', views.CustomUserViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', views.CustomLogin.as_view()),
    path('logout/', views.Logout.as_view()),
    path('social/', views.exchange_token),
    path('experience/', views.ExperienceList.as_view()),
]
urlpatterns += router.urls
