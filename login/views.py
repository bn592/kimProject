from django.shortcuts import render, redirect


# Create your views here.
from login.models import getLoginChk


def loginform(request):
    print('Method :',request.method)
    # session => T,F
    #session이 있을때는 redirect 로 list 로 보낸다.
    if 'user_id' in request.session:
        return redirect('/address/list')
    #POST로 넘어오면 = 사용자가 login 버튼을 누르면 DB안에 데이터와 비교해서 맞으면 로그인서공! 아니면 회원아니라고 뜨는 기능을 만들겠지?
    if request.method == 'POST':
        user_id = request.POST['id']
        user_pwd = request.POST['pwd']
        res = getLoginChk(id=user_id,pwd=user_pwd)
        print('*'*30)
        print(res)
        print(res[0] > 0)
        if res[0] > 0:
            print('login 성공')
            request.session['user_id'] = user_id
        else:
            print('Login Error')
            msg = "아이디 비번 오류"
            return render(request,"login/login.html",{"error":msg})
        return redirect("/login/login")

    return render(request,"login/login.html")

def logout(request):
    print("Logout처리 !")
    del request.session['user_id']
    return redirect("/login/login")