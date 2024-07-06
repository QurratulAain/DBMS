#changes
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from .forms import OrderForm

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()
    
    
    context = {
        #'orders': orders,
        'form': form,
    }
    return render(request, 'order.html', context)

def index(request):
    #usually we fetch from database and send it to context
    # context = {'variable':"this is sent"}          #context is a set of variables which is sent to template 
    #write {{variable}} in template where you wnat to send variable
    # return render(request, 'index.html',context)
    return render(request, 'index.html')
#     #return HttpResponse("this is homepage")


def contact(request):
    #return HttpResponse("this is contact page")
    return render(request, "contact.html")
    
def order(request):
    #return HttpResponse("We offer following services:")
    return render(request, "order.html")

def login(request):
    #return HttpResponse("We offer following services:")
    return render(request, "login.html")
def designer_detail(request):
    #return HttpResponse("We offer following services:")
    return render(request, "designer-detail.html")
def design_list(request):
    #return HttpResponse("We offer following services:")
    return render(request, "design-list.html")
def myaccount(request):
    #return HttpResponse("We offer following services:")
    return render(request, "my-account.html")

#def 
