from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reglog_details/',views.regLog_details,name='reglog_details'),
    path('reglog_atelier/',views.regLog_atelier,name='reglog_atelier'),
    path('reglog_tester/',views.regLog_tester,name='reglog_tester'),
    path('reglog_prediction/',views.reglog_prediction,name='reglog_prediction'),
    #random forest
    path('randforest_details/',views.randforest_details,name='randforest_details'),
    path('randforest_atelier/',views.randforest_atelier,name='randforest_atelier'),
    path('randforest_tester/',views.randforest_tester,name='randforest_tester'),
    path('randforest_prediction/',views.randforest_prediction,name='randforest_prediction'),
    #Decision Tree
    path('decTree_details/',views.decTree_details,name='decTree_details'),
    path('decTree_atelier/',views.decTree_atelier,name='decTree_atelier'),
    path('decTree_tester/',views.decTree_tester,name='decTree_tester'),
    path('decTree_prediction/',views.decTree_prediction,name='decTree_prediction'),
    #Support Vector Machine
    path('SVM_details/',views.SVM_details,name='SVM_details'),
    path('SVM_atelier/',views.SVM_atelier,name='SVM_atelier'),
    path('SVM_tester/',views.SVM_tester,name='SVM_tester'),
    path('SVM_prediction/',views.SVM_prediction,name='SVM_prediction'),

    # Decision Tree Regressor
    path('decTreeReg_atelier/',views.decTreeReg_atelier,name='decTreeReg_atelier'),
    path('decTreeReg_tester/',views.decTreeReg_tester,name='decTreeReg_tester'),
    path('decTreeReg_prediction/',views.decTreeReg_prediction,name='decTreeReg_prediction'),

    #Support Vector Machine Regréssion
    path('SVM_Reg_details/',views.SVM_Reg_details,name='SVM_Reg_details'),
    path('SVM_Reg_atelier/', views.SVM_Reg_atelier, name='SVM_Reg_atelier'),
    path('SVM_Reg_tester/',views.SVM_Reg_tester,name='SVM_Reg_tester'),
    path('SVM_Reg_prediction/',views.SVM_Reg_prediction,name='SVM_Reg_prediction'),
    #Random Forest Regression
    path('RFRatelier/', views.RFR_atelier, name='RFRatelier'),
    path('RFRtester/',views.RFR_tester,name='RFRtester'),
    path('RFRprediction/',views.RFR_prediction,name='RFRprediction'),

]