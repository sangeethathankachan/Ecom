from django.shortcuts import render,redirect
import os
from ecomapp.models import product,category,cart
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def index(request):
    
        # u_uid=request.session["uid"]
        # print(u_uid)
        pro=product.objects.all()
        return render(request,'index.html',{'pro':pro})
    

def adminindex(request):
    return render(request,'adminindex.html')

def estore(request):
    return render(request,'addcategory.html')

def addcategory(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        # items=request.FILES['file']
        data=category(categoryname=categoryname)
        data.save()
        redirect('addcategory')
    return render(request,'addcategory.html')

def addpro(request):

        cat=category.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            price=request.POST['price']
            image=request.FILES['file']
            catg1=request.POST['sel']
            categ=category.objects.get(id=catg1) 
            ctg=product(category=categ,image=image,name=name,price=price)
            ctg.save()
            return redirect('addpro')
        return render(request,'addpro.html',{'cat':cat})

# @login_required(login_url='login')
def showpro(request):
    # if 'uid' in request.session:
        pro=product.objects.all()
        return render(request,'showproduct.html',{'pro':pro})
    # return redirect('login')

def editdetails(request,pk):
    pro = product.objects.get(id=pk)
    cat = category.objects.all()
    context = {'pro':pro,'cat':cat}
    if request.method == 'POST':
        pro.name = request.POST['name']
        pro.price = request.POST['price']
        pro.image=request.FILES.get('file')
        # if request.FILES.get('file') is not None:
        #     if not pro.image == "/static/image/default.jpg":
        #         os.remove(pro.image.path)
        #         pro.image=request.FILES['file']
        #     else:
        #         pro.image=request.FILES['file']
        # else:
        #     os.remove(pro.image.path)
        #     pro.image = "/static/image/default.jpg"
        c = request.POST['sel']
        pro.category = category.objects.get(id=c)
       
        pro.save()
        return redirect(showpro)
    return render(request,'edit.html',context)

def deletedetails(request,pk):
    std=product.objects.get(id=pk)
    std.delete()
    return redirect('showpro')  
  
def logout(request):
    auth.logout(request)
    pro=product.objects.all()
    return render(request,'index.html',{'pro':pro})
    #return redirect('index')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        contact=request.POST['contact']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This user already exists!!")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password)
                user.save()
               
                return render(request,'login.html')
        else:
            messages.info(request,"Password does not match!!!")
            return redirect('signup')
        return redirect('loginpage')
    else:
        return render(request,'register.html')
    
def login_user(request):
    
    if request.method=='POST':
                    pro=product.objects.all()
                    username=request.POST['username']
                    password=request.POST['password']
                    user=auth.authenticate(username=username,password=password)
                    # request.session["uid"]=user.id
                    if user is not None:
                        if user.is_staff:
                            auth.login(request,user)
                            return render(request,'adminindex.html')
                        else:
                            # login(request,user)
                            auth.login(request,user)
                            messages.info(request,f'Welcome {username}')
                            return render(request,'index.html',{'pro':pro, 'user':user})
                            # return redirect('userhomepage')
                    else:
                        messages.info(request,'Invalid username and password')
                        return redirect('login')
    else:
                return render(request,'login.html')
            
def cartitem(request,pk,k):
    
    # print(cartitems)
    productobj= product(id=pk)
    userobj= User(id=k)
    t=cart(product=productobj,user=userobj)
    t.save()
    return redirect('index')
    # carts=cart.objects.all()
    # return render(request,'cart.html', {'cartitems':carts})
    

def loadcartitems(request,pk):
    c=cart.objects.filter(user=pk)
    return render(request,'cart.html',{'cartitems':c})

def details(request,pk,k):
    pro=product.objects.get(id=pk)
    
    return render(request,'details.html',{'pro':pro, 'u':k})

def profile(request,pk):
    std=User.objects.get(id=pk)
    
    return render(request,'profile.html',{'std':std})


def showuser(request):
        std=User.objects.filter(is_staff=0)
        return render(request,'showuser.html',{'std':std})

def deleteuser(request,pk):
    std=User.objects.get(id=pk)
    std.delete()
    return redirect('showuser')

def items(request):
    item=cart.objects.all()
    return render(request,'item.html',{'item':item})

def deleteitem(request,pk):
    item=cart.objects.get(id=pk)
    item.delete()
    return redirect('items')