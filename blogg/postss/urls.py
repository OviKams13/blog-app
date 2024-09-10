from django.urls import path
from . import views

urlpatterns = [
    path('',views.team_fc, name="team_fc"),
    path('single/<str:pk>',views.single, name="single")    
]
