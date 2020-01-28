from django.urls import path,include
from matriapp import views
urlpatterns = [
     path('',views.index),
]
