from django.urls import path
from member import views

urlpatterns = [
    path('member',views.memberJoin),
    path('meminsert',views.meminsert),
    path('memIdchk',views.memIdchk),

]