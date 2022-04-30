from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact
def index(request):
    products=Product.objects.all()
    print(products)
    param={'product':products}
    return render(request,'shop/index.html',param)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        address1=request.POST.get('Ad1','')
        address2=request.POST.get('Ad2','')
        password=request.POST.get('password','')
        city=request.POST.get('city','')
        pin_code=request.POST.get('pinc','')
        query=request.POST.get('query','')
        contact=Contact(fname=fname,lname=lname,email=email,password=password,Address1=address1,Address2=address2,city=city,pinc=pin_code,query=query)
        contact.save()
        print(fname ,lname ,email,address1,address2,password,city,pin_code,query)
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')