from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
#리퀘스트를 받아야 하니까 반드시 써줘어함.
# model 역할/ model에 담아서 html로 들고 간다.
from django.views.decorators.csrf import csrf_protect

from address.models import Address


def home(request):
    return render(request,"address/index.html")

def write(request):
    return render(request,"address/write.html")

# 가장 강력한 보안 방법 , 다른곳에서 넘어오더라도 보안이 잘 됨.
# 기본적으로 보안 해주나 @csrf_protect 달아주면 강력
# {% csrf_token %} 을 반드시 체크하는것이 기본인데 @csrf_exempt을 쓰면 스킵해버림(csrf_token 해제방법)
# form 형식으로 넘어오는 것들은 거의 post 방식으로 넘겨야함! get x , 꼭 기억!!
@csrf_protect
def insert(request):
    # get 은 http 내의 메서드 중에 하나인데 이벤트가 발행하면 원본 데이터에 변형이 없다. (단순조회 기능 )
    # post 는 이벤트를 하면 데이터의 변형이 생기는 crud 처럼 변형이 되는 경우에 쓰이는 방식임.
    print('name =>',request.POST['name'])
    print('tel =>', request.POST['tel'])
    # Address라는 객체를 만드는데 그 객체 안에 post로 받은 ['name'] 을 name에 저장.
    # 이 객체를 addr 에 저장.

    addr = Address(name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])
    #save() : 해당 모델을 생성해서 인수로 값을 전달 한 후에 insert 시킬때 사용
    # idx 를 추가 하지 않은 이유는 primary key 이기 때문 만약에 추가하면 이건 update가 됨
    addr.save() #sql문을 짜지 않아도 DB에 create table 이 되는것이 ORM 기법  .save()이 ORM 기법중에 하나임.
    return redirect('/address/list')
#render : 화면에 그린다. 표현해준다.

    #기본적인 방법이 forward
def addressListBack(request):
    print('method {}'.format(request.method))
    #address 테이블의 모든 레코드를 name 오름차순으로 저장
    # Address.odjects 하면 객체가 리스트로 저장이 되고
    # .order_by('name') : 오름차순
    # .order_by('-name') : 내림차순
    # DB에서 실행되면서 해당 Cursor 반환
    # Cursor는 메모리 공간
    # select * from address_address order by name asc
    # select * from address_address order by name desc
    # -------------------------------------------------------
    #169페이지 => Address.objects.all() : 전체 레코드들의 커서다
    #169페이지 => Address.objects.get(idx=1) : 1번을 기준으로 단일행 커서다. / detail 할 때 쓰면 될듯.
    # Address.odjects.all().count()
    # select count(*) from address_address
    #<Code 1>
    # items = Address.objects.order_by('name')
    address_count = Address.objects.all().count()
    # print('items =>{}'.format(items))
    # print('type => {}'.format(type(items)))
    #<Code 2>
    items = Address.objects.order_by('-idx')
    #page 값의 초기값이 1, 아니면 get방식으로 받는 페이지값
    # 페이지 값이 예를 들어 10이라는 값이 들어오면 10으로 저장되고, 안들어오면 1로 들어온다.
    page = int(request.GET.get('page',1))
    # 전체 데이터에서 10줄씩 분할
    pageinator = Paginator(items,'10')
    addr_list = pageinator.get_page(page)
    print('addr_list =>',addr_list)
    print('pagenaitor => ',addr_list.paginator)
    return render(request, "address/list.html"
                  ,{'address_count':address_count,'addr_list':addr_list})

def addressList(request):
    print('method {} ==>'.format(request.method))
    address_count = Address.objects.all().count()
    if request.method == 'GET':
        #items = Address.objects.order_by('-idx') #Address.objects = select * from Address / order_by('-idx'): 최신순으로 보고 싶기 때문에.
        page = int(request.GET.get('page', 1)) # 보고싶은 페이지 번호
        searchValue = request.GET.get('searchValue','') #get 으로 받은 searchValue 데이터가 없으면 공백으로 나타내라? searchValue가 혹시 내가 검색한 데이터?
        #name__icontains : 대소문자를 구분하지 않음.
        if 0 < len(searchValue) :
            items = Address.objects.filter(name__icontains=request.POST['searchValue']).order_by('-idx')
            print("Test1=============>",items,":",len(searchValue))
        else:
            items = Address.objects.order_by('-idx')
            print("Test2=============>", items, ":", len(searchValue))
        # 전체 데이터에서 10줄씩 분할
        pageinator = Paginator(items, '10') #Paginator
        addr_list = pageinator.get_page(page) # 화면 html에 그 페이지 번호만 보낸다.
        return render(request, "address/list.html"
                      , {'address_count': address_count, 'addr_list': addr_list})
    else:
        #Post 영역
        searchValue = request.POST['searchValue']
        print("searchValue =>",searchValue)
        # like %김%
        # Article.objects.filter(name__icontains='김')
        if 0 < len(searchValue) :
            items = Address.objects.filter(name__icontains=request.POST['searchValue']).order_by('-idx')
            print("Test1=============>",items,":",len(searchValue))
        else:
            items = Address.objects.order_by('-idx')
            print("Test2=============>", items, ":", len(searchValue))
        page = 1
        items = Address.objects.filter(name__icontains=request.POST['searchValue'])
        pageinator = Paginator(items, '10')
        addr_list = pageinator.get_page(page)
        return render(request, "address/list.html"
                  ,{'address_count':address_count,'addr_list':addr_list,'searchValue':searchValue})

def detail(request):
    print('*'*30)
    print("requestMethod : ", request.method)
    idv = request.GET.get('idx')
    print("Detail idx =>",idv)
    addr = Address.objects.get(idx=idv)
    print('items =>{}'.format(addr))
    print('type => {}'.format(type(addr)))
    print('name => {}'.format(addr.name))
    return render(request,'address/detail.html',{'addr':addr})

@csrf_protect
def delete(request):
    idv = request.POST['idx']
    Address.objects.get(idx=idv).delete()
    return redirect('/address/list')

@csrf_protect
def update(request):
    idv = request.POST['idx']
    # 기존에 idx값이 존재하면 수정
    addr = Address(idx=idv,name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])
    addr.save()
    return redirect('/address/detail?idx={}'.format(idv))


