from django.shortcuts import render

# Create your views here.
from member.models import memberinsert, idcheck


def memberJoin(request):
    return render(request,"member/member.html")

def meminsert(request):
    addr = (request.POST['id'], request.POST['pwd'],
            request.POST['name'], request.POST['email'],
            request.POST['tel'], request.POST['addr'],)
    # models.py 에 있는 함수를 호출 하는 것임.
    memberinsert(addr)
    return render(request,"member/success.html",{'name':request.POST['name']})

def memIdchk(request):
    idx = request.GET['id']
    res = idcheck(idx)
    print('id',res[0])
    # views.py 는 모델이니까 model에 담아서 html 로 던져준다고 생각!
    # {'res':res[0]} =>res[0]를 'res' 라는 이름으로 html 에 던져준다
    return render(request,'member/idchk.html',{'res':res[0]})

