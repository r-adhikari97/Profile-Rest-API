from django.urls import path, include
from profile_api import  views
from rest_framework.routers import DefaultRouter


# Registering a Viewset using Router
router = DefaultRouter()
router.register('hello-viewSet', views.HelloViewSets, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)


urlpatterns = [

    # Standard Function to convert API view class  to render
    path('Hello-View/',views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('',include(router.urls))

]