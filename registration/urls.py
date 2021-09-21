from django.urls import path
from . views import loginAPIView, SignupAPIView

urlpatterns = [
    path('login/',loginAPIView.as_view()),
    path('login/<int:id>/',loginAPIView.as_view()),
    path('signup/',SignupAPIView.as_view()),
    path('signup/<int:id>/',SignupAPIView.as_view()),

]
