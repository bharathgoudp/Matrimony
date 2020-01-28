from django.urls import path,include
from matriapp import views
urlpatterns = [
     path('',views.index,name='index'),
     path('myprofile/',views.myprofile,name='myprofile'),
     path('myhome/',views.myhome,name='myhome'),
     path('selfprofile/',views.selfprofile,name='selfprofile'), 
     path('photos/',views.photos,name='photos'), 
     path('profiles/',views.profiles,name='profiles'), 
     path('search/',views.search,name='search'), 
     path('step1/',views.step1,name='step1'), 
     path('step2/',views.step2,name='step2'), 
     path('step3/',views.step3,name='step3'),      
     path('step4/',views.step4,name='step4'),
]
