from django.urls import path
from profile_api import  views

urlpatterns = [

    # Standard Function to convert API view class  to render
    path('Hello-View/',views.HelloAPIView.as_view()),

]