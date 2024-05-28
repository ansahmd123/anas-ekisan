from django.shortcuts import render,redirect
from .models import AdminModel
from farmer.models import Product,Message
from accounts.models import User,Categories,Crops,Profilepic
from dealer.models import Bit,Subscription,DealerBitCounts,DealerProfilepic
from django.contrib.auth.hashers import check_password
from collections import defaultdict
from django.core.paginator import Paginator
from django.core.cache import cache
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.


def index(request):
    print('hi')
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        admin = AdminModel.objects.get(name=name)
        print(name)
        if admin is not None:
            if admin.name==name and admin.password==password:
                if admin is not None:    
                        request.session['admin_id'] = admin.id
                        return redirect('/admin/home/')
                else:
                    return render(request,'login_admin.html')
    return render(request,'login_admin.html')

def home(request):
    notification = cache.get('new_farmer_notification')
    print(notification)
    farmer_count = User.objects.filter(role='Farmer').count()
    dealer_count = User.objects.filter(role='Dealer').count()
    product_count = Product.objects.all().count()
    subscription_count=Subscription.objects.all().count()
    bits = Bit.objects.all().order_by('-created_at')[:5]
    

    context = {
        'farmer_count': farmer_count,
        'dealer_count': dealer_count,
        'bits': bits,
        'notification':notification,
        'product_count':product_count,
        'subscription_count':subscription_count
    }
    return render(request,'home_admin.html',context)

def check_new_farmer(request):
    if request.method == 'GET':
        latest_farmer = User.objects.filter(role='Farmer').latest('created_at')
        one_minute_ago = timezone.now() - timezone.timedelta(minutes=1)
        if latest_farmer.created_at > one_minute_ago:
            message = f"New farmer '{latest_farmer.name}' has been added."
            print(message)
            return JsonResponse({'message': message})
        else:
            return JsonResponse({'message': ''})


def check_new_dealer(request):
    if request.method == 'GET':
        latest_dealer = User.objects.filter(role='Dealer').latest('created_at')
        one_minute_ago = timezone.now() - timezone.timedelta(minutes=1)
        if latest_dealer.created_at > one_minute_ago:
            message = f"New dealer '{latest_dealer.name}' has been added."
            print(message)
            return JsonResponse({'message': message})
        else:
            return JsonResponse({'message': ''})

def farmer(request):
    farmer=User.objects.filter(role='Farmer')
    paginator = Paginator(farmer, 10)  # Show 10 farmers per page
    page_number = request.GET.get('page')
    farmers = paginator.get_page(page_number)
    return render(request,'farmers_admin.html',{'farmers':farmers})


def dealer(request):
    dealer=User.objects.filter(role='Dealer')
    paginator = Paginator(dealer, 10)  
    page_number = request.GET.get('page')
    dealers = paginator.get_page(page_number)
    return render(request,'dealers_admin.html',{'dealers':dealers})

def products(request):
    product=Product.objects.all()
    paginator = Paginator(product, 10)  
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request,'products_admin.html',{'products':products})

def bits(request):
    bit_list = Bit.objects.all()
    paginator = Paginator(bit_list, 10)  # Show 10 bits per page

    page_number = request.GET.get('page')
    bits = paginator.get_page(page_number)
    return render(request,'bits_admin.html',{'bits':bits})

def subscriptions(request):
    subscription_list = Subscription.objects.all()
    paginator = Paginator(subscription_list, 10)  # Show 10 subscriptions per page
    page_number = request.GET.get('page')
    subscriptions = paginator.get_page(page_number)
    return render(request,'subscription_admin.html',{'subscriptions':subscriptions})



def categories(request):
    category_list = Categories.objects.all()
    paginator = Paginator(category_list, 10)  # Show 10 categories per page

    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
    return render(request,'categories_admin.html',{'categories':categories})    

def crops(request):
    crop_list = Crops.objects.all()
    paginator = Paginator(crop_list, 10)  # Show 10 crops per page

    page_number = request.GET.get('page')
    crops = paginator.get_page(page_number)
    return render(request,'crops_admin.html',{'crops':crops})


def farmerprofilepic(request):
    profilepic_list = Profilepic.objects.all()
    paginator = Paginator(profilepic_list, 10)  
    page_number = request.GET.get('page')
    profilepics = paginator.get_page(page_number)
    return render(request,'farmerprofilepics_admin.html',{'profilepics':profilepics})


def dealerprofilepic(request):
    profilepic_list = DealerProfilepic.objects.all()
    paginator = Paginator(profilepic_list, 10)  
    page_number = request.GET.get('page')
    profilepics = paginator.get_page(page_number)
    return render(request,'dealerprofilepics_admin.html',{'profilepics':profilepics})


def message(request):
    message_list = Message.objects.all()
    paginator = Paginator(message_list, 10) 
    page_number = request.GET.get('page')
    messages = paginator.get_page(page_number)
    return render(request,'message_admin.html',{'messages':messages})

def dealerbitcount(request):
    return render(request,'dealerbitcount_admin.html')
