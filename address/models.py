from django.db import models

# Create your models here.
# models.Model 객체를 상속을 받는다.
# 지금하고 있는 거 잘알아두면 나중에 JPA? 할 때 수월
# hibenate & mybatis = ORM
# DB에서 crerate table와 동일한 기능
class Address(models.Model):
    # auto_inctement, primary_key
    idx = models.AutoField(primary_key=True)
    # idx => 인덱스 = 시퀀스번호
    # CharField => vargar2 같은것 blank => 유효성검사(front단에서 해야지.)
    name = models.CharField(max_length=50,blank=True,null=False)
    tel = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
