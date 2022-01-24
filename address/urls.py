from django.urls import path
# views에 정의한 함수를 여기서 요청과 연결
# path('url',model)
from address import views

urlpatterns = [
    path('',views.home),
    path('write',views.write), # views.py 의 write 함수를 찾아가라
    path('insert',views.insert),
    path('list',views.addressList),
    path('detail',views.detail),
    path('delete',views.delete),
    path('update',views.update),
]