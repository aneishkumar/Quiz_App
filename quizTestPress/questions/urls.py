from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('loginpage', views.loginpage),
    path('logout', views.userlogout),
    path('question/<str:userId>/<int:setId>/<int:number>/<str:home>', views.home),
    path('answer/<int:number>/<int:option>', views.answer),
    path('question/<str:userId>/<int:setId>/<int:number>', views.question),
    path('quiz/<int:userId>/<int:setId>', views.createquiz )


]