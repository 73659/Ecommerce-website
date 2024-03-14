from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Product,Cart
from django.db.models import Q

# from myapp.models import *

# Create your views here.
# def index(request):
#     return render('/index')
def index(request):
    return render(request, "index.html")

# def register(request):
#     return render(request, "register.html")
# def features(request):
#     return render(request, "features.html")

# def login(request):
#     return render(request, "login.html")
def about(request):
    return render(request, "about.html")
# def contact(request):
#     return render(request, "contact.html")
# def cart(request):
#     return render(request, "cart.html")
# def product(request):
#     return render(request, "product_details.html")
# def order(request):
#     return render(request, "orders_details.html")

def register(request):
    context={}
    if request.method=="POST":
        nm=request.POST["uname"]
        em=request.POST["uname"]
        pwd=request.POST["upassword"]
        cpwd=request.POST["cpassword"]

        # u=User.objects.create(username=nm, password=pwd)
        # u.save()
        # return HttpResponse("registration sucessfull!!!")

        if nm=="" or pwd=="" or cpwd=="":
            context['errmsg']="field can not be empty"
            return render(request, 'register.html',context)
        elif pwd !=cpwd:
            context['errmsg']='password and cpassword didnt match'
            
            return render(request,'register.html',context)

        else:
            try:
                
                u=User.objects.create(username=nm, email=em)
                u.set_password(pwd)
                u.save()
                # context['success']='User created successfully'
                # return render(request,'register.html',context)
                return HttpResponse("registration successfull!!")
            except Exception:
                context['errmsg']='Username already exist'

    else:
            
        return render(request,'register.html',context)
    
def user_login(request):
    context={}
    if request.method=="POST":
        un=request.POST["uname"]
        pwd=request.POST["upassword"]
        # print(un,pwd)
        if un=="" or pwd=="":
            context["errmsg"]="username or password can not be empty"
            return render(request, "login.html",context)
        else:
            u=authenticate(username=un,password=pwd)
            print(u)
            if u is not None:
                login(request,u)
                return redirect("/product")
            else:
                context["errmsg"]="username or password incorrect"
                return render(request,"login.html",context)
            # return HttpResponse("user checking for auth")
    else:
        return render(request, "login.html")
    
# logout page
def user_logout(request):
    print(request.user)
    logout(request)
    return redirect("/login") 

def allproducts(request):
    # p=product.objects.filter(price=2000)
    p=Product.objects.filter(is_active=True)
    context={}
    context["Products"]=p
    return render(request, "index.html", context)
    # product_list = list(p.values())
    # print(product_list)
    # return HttpResponse(product_list)

def catfilter(request, cf):
    context={}
    q1=Q(cat=cf)
    q2=Q(is_active=True)
    # product=Product.objects.filter(cat=cf)
    product=Product.objects.filter(q1&q2)
    # print(product)
    # return HttpResponse(cf)
    context["Products"]=product
    return render(request,"index.html", context)

def sortbyprice(request,sv):
    if sv =='1':
        p=Product.objects.order_by("-price").filter(is_active=True)
    else:
         p=Product.objects.order_by("price").filter(is_active=True)
    context={}
    context['Products']=p
    return render(request,'index.html', context)

def filterbyprice(request):
    mn=request.GET["min"]
    mx=request.GET["max"]
    q1=Q(price__gte=mn)
    q2=Q(price__lte=mx)
    q3=Q(is_active=True)
    prod=Product.objects.filter(q1&q2&q3)
    context={}
    context["Products"]=prod

    print(mn,mx)
    return render(request,'index.html',context)

def user(request):
    user=request.user
    return render(request,'index.html', {"user":user})

def  search(request):
    query= request.GET['query']
    p=Product.objects.filter(name__icontains=query)
    context={}
    context["Products"] = p
    context['query']=query
    return render(request, "index.html", context)
    # return HttpResponse("working!!!")

def product_details(request,pid):
    context={}
    prod=Product.objects.filter(id=pid)
    context["Product"]=prod
    return render(request,"product_details.html", context)

def cart(request, pid):
    if request.user.is_authenticated:
        uid = request.user
        product = Product.objects.get(id = pid)
        c = Cart.objects.create(user_id = uid, pid = product)
        context = {}
        context["success"] = "Product Added Successfully!!"
        return render(request, "product_details.html", context)
    
def viewcart(request):
    c = Cart.objects.filter(user_id=request.user.id)
    sum=0
    for i in c:
        sum+=i.pid.price*i.qty
    context = {'data': c}
    context["total"]=sum
    context["n"]=len(c)

    return render(request, 'cart.html', context)

def updateqty(request, x, cid):
    c=Cart.objects.filter(id=cid)
    q=c[0].qty
    if x == "1":
        q=q+1
    elif q>1:
        q=q-1
    c.update(qty=q)
    return redirect('/viewcart')

def removecart(request, cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')

def placeorder(request):
    return render(request,'placeorder.html')
    
    
    
