from django.urls import path
# views에 정의한 함수를 여기서 요청과 연결
# path('url',model)
from login import views

urlpatterns = [
    path('login',views.loginform),
    path('logout', views.logout),

]