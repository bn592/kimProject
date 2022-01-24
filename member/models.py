from django.db import models
#pip install cx_oracle
import cx_Oracle as ora
database = 'kosmo100/kosmo100@192.168.56.1/xe'
# Create your models here.
'''
public void insert(MemberVO vo){
    Connection con = MyConn.getConn();
    PreparedeStatement psmt = con.preparedStatementd();
    String sql = "insert into member values(member_seq.nextVal,?,?,sysdate)";
    psmt.setString(1,vo.getId());
    psmt.setInt(2,vo.getAge());
    psmt.executeUpdate();
    .....
}
'''
# views.py에서 받은 addr_list를 오라클 db에 올린다.
def memberinsert(addr_list):
    #오라클 접속
    conn = ora.connect(database)
    #prepareled statesment
    cursor = conn.cursor()
    print('conn =>',cursor)
    # num,id,pwd,name,email,tel,addr,mdate
    # :1,:2,:3,:4,:5,:6, 이게 무슨 방법 이라고? 받은 리스트를 하나씩 뽑아내는 바인딩 방식
    sql = "insert into member values(member_seq.nextVal,:1,:2,:3,:4,:5,:6,sysdate)"
    #맵핑후 오라클 쿼리로 전송
    cursor.execute(sql,addr_list)
    cursor.close()
    conn.commit()
    conn.close()

def idcheck(idx):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select count(*) from member where id=:id"
    cursor.execute(sql,id=idx)
    # fetchone() 단일커서, 단일 행 일 때 사용한다. 상세보기
    # fetchall() 다중행 커서, 다중행 일 때 사용한다. 전체보기
    res = cursor.fetchone()
    print('res =======>',res)
    cursor.close()
    conn.close()
    return res
