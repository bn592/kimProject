from django.db import models

# Create your models here.
import cx_Oracle as ora
database = 'kosmo100/kosmo100@192.168.56.1/xe'

def getLoginChk(**kwargs):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select count(*) cnt from member where id=:id" \
          " and pwd=:pwd"
    cursor.execute(sql,id=kwargs['id'], pwd=kwargs['pwd'])
    datas = cursor.fetchone()
    cursor.close()
    conn.close()
    return datas