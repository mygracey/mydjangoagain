from django.shortcuts import render,redirect

# Create your views here.


def indexPage(request):
    return render(request,'index.html')



def registerPage(request):
    return render(request,'register.html')



def productsPage(request):
    return render(request,'products.html')



def logoutPage(request):
    pass
