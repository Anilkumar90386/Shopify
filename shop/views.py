from django.shortcuts import render
from . models import Product,Contact,Order,Buy
from math import ceil
# Create your views here.
from django.http import HttpResponse
def index(request):
    # product=Product.objects.all()
    # n=len(product)
    # nSlides=n//5+ceil((n/5)-(n//5))
    #params={'no_of_slides':nSlides,'range':range(nSlides),'product':product}
    #allProds=[[product,range(1,nSlides),nSlides],[product,range(1,nSlides),nSlides]]
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//5+ceil((n//5)-(n//5))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def searchMatch(query,item):
    if query in item.desc or query in item.product_name or query in item.category:
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search')
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prod)
        nSlides=n//5+ceil((n//5)-(n//5))
        if len(prod) !=0:
            allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')

def checkout(request):
    if request.method=="POST":
        order_name=request.POST.get('order_name')
        order_email=request.POST.get('order_email')
        order_phone=request.POST.get('order_phone')
        order_city=request.POST.get('order_city')
        order_state=request.POST.get('order_state')
        order_zip=request.POST.get('order_zip')
        order=Order(order_name=order_name,order_email=order_email,order_phone=order_phone,order_city=order_city,order_state=order_state,order_zip=order_zip)
        order.save()
    return render(request,'shop/check.html')
def productview(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/product.html',{'product':product[0]})

def Buying(request):
    buy_price=request.GET.get("product_price")
    print(buy_price)
    return render(request,'shop/product_price.html')

