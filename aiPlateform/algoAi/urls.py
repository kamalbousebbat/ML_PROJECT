from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reglog_details/',views.regLog_details,name='reglog_details'),
    path('reglog_atelier/',views.regLog_atelier,name='reglog_atelier'),
    path('reglog_tester/',views.regLog_tester,name='reglog_tester'),
    path('reglog_prediction/',views.reglog_prediction,name='reglog_prediction'),
]