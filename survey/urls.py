from django.urls import path

from survey import views

urlpatterns = [
    path('',views.surveyList),
    path('save_survey',views.save_survey),
    path('show_result', views.show_result),
    path('chartdemo1', views.chartdemo1),
    path('chartpractice1', views.chartpractice1),

]