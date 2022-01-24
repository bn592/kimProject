from django.shortcuts import render, redirect

# Create your views here.
from shop.models import Product


def product_write(request):
    return render(request,"shop/product_write.html")
#터미널에서 경로를 pwd로 확인 후 복사해옴. 앞으로 가져오는 사진을 이 경로에 자동저장되게 할거야.
UPLOAD_DIR = '/home/kosmo100/ws/mykosjango/shop/static/images/'
def product_insert(request):
    # html에서 name="file1" 인 애가 request로 들어옴.
    product_name = request.POST['product_name']
    # file name, file size 함께 전송되어 온다.
    #file = request.FILES['file1']
    #print('file_name => ',file._name)
    #print('file_size => ',file._size)
    #print('type{}, pname=> {}'.format(file,product_name))
    print('*' * 30)
    print(request.FILES)
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        fp = open(UPLOAD_DIR + file_name,'wb')
        # chunks는 1byte단위로 읽어들이는 함수다.
        for chunk in file.chunks():
            # 이게 파일 저장하는거였나?
            fp.write(chunk)
        fp.close()
    else:
        # file_name 의 '-' 이거 뭐였지? file에 이미지가 없다면?
        # 이미지가 없다면 DB picture_url 컬럼에 - 이 들어온다는 의
        file_name = '-'
    dto = Product(product_name=request.POST['product_name'],
                  price=request.POST['price'],
                  description=request.POST['description'],
                  picture_url=file_name)
    dto.save()
    # 근데 왜 내용도 없는데(success.html) 이 경로를 지정해주는거죠? 오류 안나게한다고요?
    return redirect('/shop/product_list')

def product_list(request):
    count = Product.objects.count()
    productList = Product.objects.order_by("-product_id")
    return render(request,"shop/product_list.html",
                  {"productList":productList,"count":count})
