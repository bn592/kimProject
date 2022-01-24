from django.contrib import admin

# Register your models here.
# admin과 관련될 모델
#from ddjango.contrib.admin imoirt ModelAdmin(위에 있는 import와 동일함.)
#OCP
from address.models import Address

# admin이 가장 처음 돌아가는 최상단.
class Address_Admin(admin.ModelAdmin):
    #admin UI add()
    #번호는 자동관리
    list_display = ('name','tel','email','address') # 화면에 출력해주고 싶은 열들.
# admin에 등록하기 위해서 register 메서드를 호출한다.
# 이때 모델과 display를 함께 등록
admin.site.register(Address,Address_Admin)

