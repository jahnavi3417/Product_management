from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

from.models import Product,Category
from.forms import ProductForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# to view all the product in the showproduct.html


def ShowAllProducts(request):
    category=request.GET.get('category') # get the clicked category name:mobile

    if category==None:
        products=Product.objects.filter(is_published=True).order_by('-price')
    else:
        products=Product.objects.filter(category__name=category)


    # products=Product.objects.filter(is_published=True).order_by('price')
    num_product=Product.objects.all().count()
    page_num=request.GET.get('page') #creating the total pages
    paginator = Paginator(products,3) # seting total number of products in a page:3
    try:
        products=paginator.page(page_num)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages )

    categories=Category.objects.all()
 
    context={ 
        'products':products,
        'num_product':num_product,
        'categories':categories
    }
    return render (request,'showProducts.html',context)


def Byproduct(request,pk):
    eachproduct=Product.objects.get(id=pk)
    context={
        'eachproduct':eachproduct
    }
    return render(request,'by_products.html',context)


# to view the single product details in this productdetails.html
# @login_required(login_url='accounts/login')
def productDetail(request,pk):
    eachproduct=Product.objects.get(id=pk)
    context={
        'eachproduct':eachproduct
    }
    return render(request,'productDetail.html',context)

#to Add the new product from  the html templates page add.html

@login_required(login_url='ShowProducts')
def addProduct(request):
    form=ProductForm()

    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ShowProducts')

    context={
        'form':form
        }
    return render(request,'addProduct.html',context)



# to update the product form from the html templte page update product .html

@login_required(login_url='ShowProducts')
def updateProduct(request,pk):
    product=Product.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect("ShowProducts")
    context={
        'form':form
    }
    return render(request,'updateProduct.html',context)



# delete the record from the database from the table, base on the primary keywe can use uniquee key

@login_required(login_url='ShowProducts')
def deleteProduct(request,pk):
    product=Product.objects.get(id=pk) #storing record of 1 or 2 or 3 in products
    product.delete() #1=delete
    return redirect("ShowProducts")


#creating a function for searching the data from the data base using the keywords

# @login_required(login_url='ShowProducts')
def SearchBar(request):
    if request.method=='GET':  #get=GET==TRUE
        query = request.GET.get('query') #query=999
        if query:
            products=Product.objects.filter(name__contains=query)
            return render(request,'searchbar.html',{'products':products})
        else:
            print("no products Found to show in the data base")
            return render(request,'searchbar.html',{})
        

def Address(request):
    form=ProductForm()

    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ShowProducts')

    context={
        'form':form
        }
    return render(request,'continue.html',context)


@login_required(login_url='ShowProducts')
def user(request,pk):
    userupdate=Product.objects.get(id=pk)
    context={
        'userupdate':userupdate
    }
    return render(request,'user.html',context)