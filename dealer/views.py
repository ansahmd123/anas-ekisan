from django.shortcuts import render,redirect
from accounts.models import User,Subscription,Categories,Crops
from farmer.models import Product,Tracking
from django.shortcuts import render, get_list_or_404
from dealer.models import Bit,DealerProfilepic,DealerBitCounts
from django.http import JsonResponse,HttpResponse
from farmer.models import Message
import razorpay
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
import os
# Create your views here.
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.http import Http404


def buy(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        categories=Categories.objects.all()       
        return render(request,'buy_dealer.html',{'user_name':user_name,'categories':categories})

#     user_id = request.session.get('user_id')

#     if user_id:
#         user = User.objects.get(pk=user_id)
#         user_name = user.name

#         # Check user's subscription
#         user_subscription = Subscription.objects.filter(user=user).first()
#         if user_subscription:
#                 has_added_product = Bit.objects.filter(bitter=user_name).exists()
                
#                 if has_added_product:
#                         return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only one product with a free subscription.'})
                
#                 current_date = datetime.now().date()
#                 expiry_date = user_subscription.date + timedelta(days=3)
#                 if current_date > expiry_date:
#                         Product.objects.filter(user=user).delete()
#                         return render(request, 'subscription_dealer.html')

#                 return render(request,'buy_dealer.html',{'user_name':user_name})
        
#         elif user_subscription.planname == 'basic':
#                 # For basic subscription, dealer can buy only 4 products and they expire after 30 days
                
#                 product_count = Bit.objects.filter(bitter=user_name).count()
#                 if product_count >= 4:
#                         return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only 4 products with a basic subscription.'})
                
#                 current_date = datetime.now().date()
#                 expiry_date = user_subscription.date + timedelta(days=30)
#                 if current_date > expiry_date:
#                         Product.objects.filter(user=user).delete()
#                         return render(request, 'subscription_dealer.html')

#                 return render(request,'buy_dealer.html',{'user_name':user_name})

#         elif user_subscription.planname == 'standard':
                
#                 product_count = Bit.objects.filter(bitter=user_name).count()
#                 if product_count >= 10:
#                         return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only 10 products with a basic subscription.'})
                
#                 current_date = datetime.now().date()
#                 expiry_date = user_subscription.date + timedelta(days=30)
#                 if current_date > expiry_date:
#                         Product.objects.filter(user=user).delete()
#                         return render(request, 'subscription_dealer.html')

#                 return render(request,'buy_dealer.html',{'user_name':user_name})

#         elif user_subscription.planname == 'premium':
                
#                 current_date = datetime.now().date()
#                 expiry_date = user_subscription.date + timedelta(days=30)
#                 if current_date > expiry_date:
#                         Product.objects.filter(user=user).delete()
#                         return render(request, 'subscription_dealer.html')

#                 return render(request,'buy_dealer.html',{'user_name':user_name})

                 
#     # Handle the case where user_id is None
#     user_id = request.session.get('user_id')
#     if user_id is not None:
#         profile = User.objects.get(id=user_id)
#         try:        
#                 subscription=Subscription.objects.get(user=user_id)
#                 plantype=subscription.planname
#                 date=subscription.date
#                 if plantype=='free':
#                     expiry_date=date + timedelta(days=3)
#                     if (subscription is not None):
#                         return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
#                 else:
#                     expiry_date=date + timedelta(days=30)
#                     if (subscription is not None):
#                         return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})    
#         except ObjectDoesNotExist:
#                 return render(request, 'dealerprofile_dealer.html', {'profile': profile})




def addbuy(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request, 'addbuy_dealer.html',{'user_name':user_name})

def vegitables(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request,'vegitables_dealer.html',{'user_name':user_name}) 

def fruits(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request,'fruits_dealer.html',{'user_name':user_name}) 

def crops(request,id):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        crops=Crops.objects.filter(category=id)  
        for crop in crops:
               name=crop.nameineng
               farmer=Product.objects.filter(product_name=name).count()    
        return render(request,'subcategories_dealer.html',{'user_name':user_name,'crops':crops,'farmer':farmer}) 



def herb(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'herb_dealer.html',{'user_name':user_name}) 


def nuts(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'nuts_dealer.html',{'user_name':user_name}) 

def grains(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'grains_dealer.html',{'user_name':user_name}) 


def legumes(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'legumes_dealer.html',{'user_name':user_name}) 


def tubers(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'tubers_dealer.html',{'user_name':user_name}) 


def berries(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'berries_dealer.html',{'user_name':user_name}) 


def flowers(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'flowers_dealer.html',{'user_name':user_name}) 


def leafygreens(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'leafygreens_dealer.html',{'user_name':user_name}) 


def roots(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'roots_dealer.html',{'user_name':user_name}) 



def spices(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'spices_dealer.html',{'user_name':user_name}) 



def medicinalplants(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'medicinalplants_dealer.html',{'user_name':user_name}) 



def mushrooms(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'mushrooms_dealer.html',{'user_name':user_name}) 



def pulses(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'pulses_dealer.html',{'user_name':user_name}) 




def oilseeds(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'oilseeds_dealer.html',{'user_name':user_name}) 


def covercrops(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'covercrops_dealer.html',{'user_name':user_name}) 



def condiments(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'condiments_dealer.html',{'user_name':user_name}) 



def exoticplants(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'exoticplants_dealer.html',{'user_name':user_name}) 



def dealers(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    farmers = User.objects.filter(role='Farmer')
    return render(request, 'dealers_dealer.html', {'farmers': farmers,'user_name':user_name})

def dealersprofile(request):
        try:
                user_id = request.session.get('user_id')
                profile = User.objects.get(id=user_id)
                profilepic = None
                subscription=Subscription.objects.filter(user=profile) 
                profilepic=DealerProfilepic.objects.get(user=profile)       
                print('hi',subscription)
                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
        except Subscription.DoesNotExist:
                user_id = request.session.get('user_id')
                profile = User.objects.get(id=user_id)
                profilepic = None
                profilepic=DealerProfilepic.objects.get(user=profile)
                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
        except DealerProfilepic.DoesNotExist:
                user_id = request.session.get('user_id')
                profile = User.objects.get(id=user_id)
                profilepic = None
                subscription=Subscription.objects.filter(user=profile)
                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
        
        
def editdealerprofile(request,id):
       dealer=User.objects.get(id=id)
       return render(request,'editdealerprofile_dealer.html',{'dealer':dealer})       

def updatedealerprofile(request,id):
       user=User.objects.get(id=id)
       if request.method=='POST':
              user.name=request.POST['name']
              user.address=request.POST['address']
              user.city=request.POST['city']
              user.state=request.POST['state']
              user.email=request.POST['email']
              user.save()
              user_id = request.session.get('user_id')
              if user_id is not None:
                        profile = User.objects.get(id=user_id)
                        try:        
                                subscription=Subscription.objects.get(user=user_id)
                                plantype=subscription.planname
                                date=subscription.date
                                expiry_date=subscription.expiry_date
                                if plantype=='free':
                                        if (subscription is not None):
                                                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription})
                                else:
                                        expiry_date=date + timedelta(days=30)
                                        if (subscription is not None):
                                                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription})    
                        except ObjectDoesNotExist:
                         return render(request, 'dealerprofile_dealer.html', {'profile': profile})
              else:
                        return render(request, 'index.html')       
       return redirect(('dealerprofile')) 


def changepassword(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        # Retrieve the hashed password from the database
        password_from_db = user.password
        
        if new_password == confirm_new_password:
                # Verify the current password
                if check_password(current_password, user.password):
                        # Hash the new password before saving it
                        hashed_password = make_password(new_password)
                        user.password = hashed_password
                        user.save()
                        messages = 'Password successfully changed.'

                        user_id = request.session.get('user_id')
                        if user_id is not None:
                                profile = User.objects.get(id=user_id)
                                try:        
                                        subscription=Subscription.objects.get(user=user_id)
                                        plantype=subscription.planname
                                        date=subscription.date
                                        expiry_date=subscription.expiry_date
                                        if plantype=='free':
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'messages':messages})
                                        else:
                                                expiry_date=date + timedelta(days=30)
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'messages':messages})    
                                except ObjectDoesNotExist:
                                        profile = User.objects.get(id=user_id)
                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'messages':messages})
                        else:
                                return render(request, 'index.html')   
        return render(request, 'dealerprofile_dealer.html')


def dealerprofilepic(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        try:    
                
                profile=DealerProfilepic.objects.get(user=user)
                if profile:
                        profile.profilepic=request.FILES['profilepic']
                        profile.save()
                        file_name = profile.profilepic.name
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        with open(file_path, 'wb') as destination:
                                for chunk in profile.profilepic.chunks():
                                        destination.write(chunk)  
                        user_id = request.session.get('user_id')
                        if user_id is not None:
                                profile = User.objects.get(id=user_id)
                                try:        
                                        subscription=Subscription.objects.get(user=user_id)
                                        plantype=subscription.planname
                                        date=subscription.date
                                        expiry_date=subscription.expiry_date
                                        profilepic=DealerProfilepic.objects.get(user=user)
                                        if plantype=='free':
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                        else:
                                                expiry_date=date + timedelta(days=30)
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                                except ObjectDoesNotExist:
                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic})
                        else:
                                return render(request, 'index.html') 
                else:
                    profilepic=request.FILES['profilepic']
                    profile=DealerProfilepic(profilepic=profilepic,user=user)
                    profile.save() 
                    file_name = profile.profilepic.name
                    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                    with open(file_path, 'wb') as destination:
                            for chunk in profile.profilepic.chunks():
                                    destination.write(chunk)  
                    user_id = request.session.get('user_id')
                    if user_id is not None:
                            profile = User.objects.get(id=user_id)
                            try:        
                                    subscription=Subscription.objects.filter(user=user_id)
                                    for subscription in subscription:
                                        plantype=subscription.planname
                                        date=subscription.date
                                        expiry_date=subscription.expiry_date
                                        if plantype=='free':
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                        else:
                                                expiry_date=date + timedelta(days=30)
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                            except ObjectDoesNotExist:
                                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic})
                    else:
                            return render(request, 'index.html')                     

        except:                        
                print('hey')
                profilepic=request.FILES['profilepic']
                profile=DealerProfilepic(profilepic=profilepic,user=user)
                profile.save() 
                file_name = profile.profilepic.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                with open(file_path, 'wb') as destination:
                        for chunk in profile.profilepic.chunks():
                                destination.write(chunk)  
                user_id = request.session.get('user_id')
                if user_id is not None:
                        profile = User.objects.get(id=user_id)
                        try:        
                                subscription=Subscription.objects.filter(user=user_id)
                                for subscription in subscription:
                                        plantype=subscription.planname
                                        date=subscription.date
                                        expiry_date=subscription.expiry_date
                                        if plantype=='free':
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                        else:
                                                expiry_date=date + timedelta(days=30)
                                                if (subscription is not None):
                                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                        except ObjectDoesNotExist:
                                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic})
                else:
                        return render(request, 'index.html')        
        return render(request,'dealerprofile_dealer.html')




def delivery(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        user_name=profile.name
    if user_id:    
        bits = Bit.objects.filter(bitter=user_name)
        if bits.exists():
            first_bit = bits.first()
            farmer = first_bit.farmer
        else:
            farmer = None
        farmer= User.objects.get(name=farmer)
        user_id=farmer.id
        product=Product.objects.get(user_id=user_id)
        quantity=product.quantity
        bit = Bit.objects.get(bitter=user_name)
        name=bit.product
        amount=bit.bit_value
        amount=int(amount)
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        charge=float(amount)*0.05
        quantity_numeric =  quantity
        yourAmount=amount
        amount=amount*quantity_numeric
        charge=charge*quantity_numeric
        user_id=request.session.get('user_id')
        user=User.objects.get(id=user_id)
        address=user.address
        user_name = user.name
        paymentAmount=int(yourAmount)*int(quantity_numeric)
        delivery_charge=float(yourAmount)*0.10*float(quantity_numeric)
        total=float(paymentAmount)+float(charge)+float(delivery_charge)
        pay=total*100
        return render(request,'delivery_dealer.html',{'total':total,'pay':pay,'amount':amount,'quantity':quantity,'yourAmount':yourAmount,'paymentAmount':paymentAmount,'delivery_charge':delivery_charge,'charge':charge,'name':name,'address':address,'user_name':user_name})
    return render(request, 'delivery_dealer.html')


def deliverymenadd(request):
    return render(request, 'deliverymenadd_dealer.html')

def deliverymenedit(request):
    return render(request, 'deliverymenedit_dealer.html')

def farmerslist(request):
    return render(request, 'farmerslist_dealer.html')

def farmersadd(request):
    return render(request, 'farmersadd_dealer.html')    
    
def farmersedit(request):
    return render(request, 'farmersedit_dealer.html') 

def productcategory(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name   
    return render(request, 'productcategory_dealer.html',{'user_name':user_name})

def productcategorylist(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name   
    user=User.objects.get(id=user_id)
    name=user.name
    products=Bit.objects.filter(bitter=name,status=True) 
    print(products)  
    return render(request, 'productcategorylist_dealer.html',{'user_name':user_name,'products':products})
   
def productlist(request,fruit):
        try:
                user_id = request.session.get('user_id')
                if user_id:
                        user = User.objects.get(pk=user_id)
                        user_name = user.name
                fruit_data = get_list_or_404(Product, product_name=fruit)
                return render(request, 'productlist_dealer.html', {'fruit_data': fruit_data, 'fruit': fruit,'user_name':user_name})
        except Http404:
                fruit_data = []  
                user_id = request.session.get('user_id')
                if user_id:
                        user = User.objects.get(pk=user_id)
                        user_name = user.name
                return render(request, 'productlist_dealer.html', {'fruit_data': fruit_data, 'fruit': fruit,'user_name':user_name})
        
        
def transactions(request):
    return render(request, 'transactionsdealer_dealer.html')    

def bit(request, user_id, user_name, product_name, product_type, quality, rate, quantity):
     context = {
        'user_id': user_id,     
        'user_name': user_name,
        'product_name': product_name,
        'product_type': product_type,
        'quality': quality,
        'rate': rate,
        'quantity': quantity,
    }
     return render(request,'bit_dealer.html',context)

def process_bit(request,id):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
        bitter_address=user.address
        if user_id:
                        user = User.objects.get(pk=user_id)
                        user_name = user.name
                        user_subscription = Subscription.objects.get(user=user, planname='free')
                        try:
                                dealer_profile = DealerBitCounts.objects.get(user=user,subscription_plan=user_subscription)
                        except DealerBitCounts.DoesNotExist:        
                                if request.method == 'POST':
                                                farmer = request.POST.get('farmer')
                                                product = request.POST.get('product')
                                                product_type = request.POST.get('product_type')
                                                quality = request.POST.get('quality')
                                                rate = request.POST.get('rate')
                                                quantity = request.POST.get('quantity')
                                                bit_value = request.POST.get('bit')
                                                status = False
                                                farmer=User.objects.get(name=farmer)
                                                farmer_address=farmer.address
                                                user_ids=User.objects.get(id=id)
                                                Bit.objects.create(
                                                farmer_id=user_ids,   
                                                farmer=farmer,
                                                product=product,
                                                product_type=product_type,
                                                quality=quality,
                                                rate=rate,
                                                quantity=quantity,
                                                bit_value=bit_value,
                                                bitter=user_name,
                                                status=status,
                                                bitter_address=bitter_address,
                                                farmer_address=farmer_address
                                                )
                                                DealerBitCounts.objects.create(user=user,subscription_plan=user_subscription,current_bid_count=1)
                                                return redirect('mybits')
                                else:
                                        
                                        return render(request, 'cantbuy_dealer.html',{'error_message': 'You can add only one product with a free subscription.'}) 
                        basic_subscription = Subscription.objects.filter(user=user, planname='basic').first()
                        if basic_subscription:
                                user_subscription = basic_subscription
                                try:
                                        dealer_profile = DealerBitCounts.objects.get(user=user,subscription_plan=user_subscription)
                                        if dealer_profile.current_bid_count <= 4:
                                                if request.method == 'POST':
                                                        farmer = request.POST.get('farmer')
                                                        product = request.POST.get('product')
                                                        product_type = request.POST.get('product_type')
                                                        quality = request.POST.get('quality')
                                                        rate = request.POST.get('rate')
                                                        quantity = request.POST.get('quantity')
                                                        bit_value = request.POST.get('bit')
                                                        status = False
                                                        farmer=User.objects.get(name=farmer)
                                                        farmer_address=farmer.address
                                                        user_ids=User.objects.get(id=id)
                                                        Bit.objects.create(
                                                        farmer_id=user_ids,   
                                                        farmer=farmer,
                                                        product=product,
                                                        product_type=product_type,
                                                        quality=quality,
                                                        rate=rate,
                                                        quantity=quantity,
                                                        bit_value=bit_value,
                                                        bitter=user_name,
                                                        status=status,
                                                        bitter_address=bitter_address,
                                                        farmer_address=farmer_address
                                                        )
                                                        dealer_profile.current_bid_count += 1
                                                        dealer_profile.save()
                                                        return redirect('mybits')
                                        else:
                                                return render(request, 'cantbuy_dealer.html',{'error_message': 'You can add only four product with a basic subscription plan.'})        
                                except DealerBitCounts.DoesNotExist:
                                        if request.method == 'POST':
                                                farmer = request.POST.get('farmer')
                                                product = request.POST.get('product')
                                                product_type = request.POST.get('product_type')
                                                quality = request.POST.get('quality')
                                                rate = request.POST.get('rate')
                                                quantity = request.POST.get('quantity')
                                                bit_value = request.POST.get('bit')
                                                status = False
                                                farmer=User.objects.get(name=farmer)
                                                farmer_address=farmer.address
                                                user_ids=User.objects.get(id=id)
                                                Bit.objects.create(
                                                farmer_id=user_ids,   
                                                farmer=farmer,
                                                product=product,
                                                product_type=product_type,
                                                quality=quality,
                                                rate=rate,
                                                quantity=quantity,
                                                bit_value=bit_value,
                                                bitter=user_name,
                                                status=status,
                                                bitter_address=bitter_address,
                                                farmer_address=farmer_address
                                                )
                                                return redirect('mybits')                               
                        standard_subscription = Subscription.objects.filter(user=user, planname='standard').first()
                        if standard_subscription:
                                user_subscription = standard_subscription
                                try:
                                        dealer_profile = DealerBitCounts.objects.get(user=user,subscription_plan=user_subscription)
                                        if dealer_profile.current_bid_count <= 10:
                                                if request.method == 'POST':
                                                        farmer = request.POST.get('farmer')
                                                        product = request.POST.get('product')
                                                        product_type = request.POST.get('product_type')
                                                        quality = request.POST.get('quality')
                                                        rate = request.POST.get('rate')
                                                        quantity = request.POST.get('quantity')
                                                        bit_value = request.POST.get('bit')
                                                        status = False
                                                        farmer=User.objects.get(name=farmer)
                                                        farmer_address=farmer.address
                                                        user_ids=User.objects.get(id=id)
                                                        Bit.objects.create(
                                                        farmer_id=user_ids,   
                                                        farmer=farmer,
                                                        product=product,
                                                        product_type=product_type,
                                                        quality=quality,
                                                        rate=rate,
                                                        quantity=quantity,
                                                        bit_value=bit_value,
                                                        bitter=user_name,
                                                        status=status,
                                                        bitter_address=bitter_address,
                                                        farmer_address=farmer_address
                                                        )
                                                        dealer_profile.current_bid_count += 1
                                                        dealer_profile.save()
                                                        return redirect('mybits')
                                except DealerBitCounts.DoesNotExist:
                                        if request.method == 'POST':
                                                farmer = request.POST.get('farmer')
                                                product = request.POST.get('product')
                                                product_type = request.POST.get('product_type')
                                                quality = request.POST.get('quality')
                                                rate = request.POST.get('rate')
                                                quantity = request.POST.get('quantity')
                                                bit_value = request.POST.get('bit')
                                                status = False
                                                farmer=User.objects.get(name=farmer)
                                                farmer_address=farmer.address
                                                user_ids=User.objects.get(id=id)
                                                Bit.objects.create(
                                                farmer_id=user_ids,   
                                                farmer=farmer,
                                                product=product,
                                                product_type=product_type,
                                                quality=quality,
                                                rate=rate,
                                                quantity=quantity,
                                                bit_value=bit_value,
                                                bitter=user_name,
                                                status=status,
                                                bitter_address=bitter_address,
                                                farmer_address=farmer_address
                                                )
                                                return redirect('mybits')
                        premium_subscription = Subscription.objects.filter(user=user, planname='premium').first()
                        if premium_subscription:
                                user_subscription = premium_subscription
                                try:
                                        dealer_profile = DealerBitCounts.objects.get(user=user,subscription_plan=user_subscription)
                                        if dealer_profile.current_bid_count <= 10:
                                                if request.method == 'POST':
                                                        farmer = request.POST.get('farmer')
                                                        product = request.POST.get('product')
                                                        product_type = request.POST.get('product_type')
                                                        quality = request.POST.get('quality')
                                                        rate = request.POST.get('rate')
                                                        quantity = request.POST.get('quantity')
                                                        bit_value = request.POST.get('bit')
                                                        status = False
                                                        farmer=User.objects.get(name=farmer)
                                                        farmer_address=farmer.address
                                                        user_ids=User.objects.get(id=id)
                                                        Bit.objects.create(
                                                        farmer_id=user_ids,   
                                                        farmer=farmer,
                                                        product=product,
                                                        product_type=product_type,
                                                        quality=quality,
                                                        rate=rate,
                                                        quantity=quantity,
                                                        bit_value=bit_value,
                                                        bitter=user_name,
                                                        status=status,
                                                        bitter_address=bitter_address,
                                                        farmer_address=farmer_address
                                                        )
                                                        dealer_profile.current_bid_count += 1
                                                        dealer_profile.save()
                                                        return redirect('mybits')
                                except DealerBitCounts.DoesNotExist:
                                        if request.method == 'POST':
                                                farmer = request.POST.get('farmer')
                                                product = request.POST.get('product')
                                                product_type = request.POST.get('product_type')
                                                quality = request.POST.get('quality')
                                                rate = request.POST.get('rate')
                                                quantity = request.POST.get('quantity')
                                                bit_value = request.POST.get('bit')
                                                status = False
                                                farmer=User.objects.get(name=farmer)
                                                farmer_address=farmer.address
                                                user_ids=User.objects.get(id=id)
                                                Bit.objects.create(
                                                farmer_id=user_ids,   
                                                farmer=farmer,
                                                product=product,
                                                product_type=product_type,
                                                quality=quality,
                                                rate=rate,
                                                quantity=quantity,
                                                bit_value=bit_value,
                                                bitter=user_name,
                                                status=status,
                                                bitter_address=bitter_address,
                                                farmer_address=farmer_address
                                                )
                                                return redirect('mybits')
    return render(request,'buy_dealer.html')


def mybits(request):
        try:
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            name=user.name
            print('hi',name)
            bit_data = Bit.objects.filter(bitter=name).values('product','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value')
            print('het',bit_data)
            bit = {}
            for entry in bit_data:
                product_name = entry['product']
                if product_name not in bit or product_name in bit:
                        bit[product_name] = []
                        bit[product_name].append(entry)
            
            notifications = Message.objects.filter(user=user)

            context = {
                        'bit': bit,
                        'bit_data':bit_data,
                        #'user_name':user_name,
                        'notifications':notifications
                }
            return render(request,'mybits_dealer.html',context)
        except Bit.DoesNotExist:
                return render(request, 'error.html', {'message': 'Bit not found'})
        

from django.core.exceptions import ObjectDoesNotExist

def get_notifications(request):
        try:
            id=request.session.get('user_id')
            user = User.objects.get(id=id)
            user_notifications = Message.objects.filter(user=user.name).values('notification', 'product')
            notifications = [{'notification': notification['notification'], 'product': notification['product']} for notification in user_notifications]
            bit_value = Bit.objects.filter(bitter=user.name)
            for bit_value in bit_value:    
                quantity = bit_value.quantity
            return JsonResponse({'notifications': notifications, 'bit_value': bit_value.bit_value, 'quantity': quantity})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Bit object does not exist for the current user'})
        


def pay(request,amount,name,quantity):
    charge=amount*0.05
    quantity_numeric = float(''.join(filter(str.isdigit, quantity)))
    yourAmount=amount
    amount=amount*quantity_numeric
    charge=charge*quantity_numeric
    client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
    payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    address=user.address
    user_name = user.name
    paymentAmount=amount*quantity_numeric
    delivery_charge=yourAmount*0.10*quantity_numeric
    total=amount+charge+delivery_charge
    pay=total*100
    return render(request,'pay_dealer.html',{'total':total,'pay':pay,'amount':amount,'quantity':quantity,'yourAmount':yourAmount,'paymentAmount':paymentAmount,'delivery_charge':delivery_charge,'charge':charge,'name':name,'address':address,'user_name':user_name})


def subscription(request):
        try:
                user_id=request.session.get('user_id') 
                profile=User.objects.get(id=user_id)
                subscription=Subscription.objects.filter(user=profile)
                profilepic=DealerProfilepic.objects.get(user=profile) 
                print('hi',subscription)
                return render(request, 'dealerprofile_dealer.html', {'profilepic':profilepic,'profile':profile,'subscription':subscription})                       
        except DealerProfilepic.DoesNotExist:
                user_id=request.session.get('user_id') 
                profile=User.objects.get(id=user_id)
                subscription=Subscription.objects.filter(user=profile)
                if subscription:
                        return render(request, 'dealerprofile_dealer.html', {'profile':profile,'subscription':subscription})
                else:   
                        user_id=request.session.get('user_id')
                        user=User.objects.get(id=user_id)
                        name=user.name     
                        return render(request,'subscription_dealer.html',{'name':name})        
        except Subscription.DoesNotExist:
                 user_id=request.session.get('user_id')
                 user=User.objects.get(id=user_id)
                 name=user.name
                 return render(request,'subscription_dealer.html',{'name':name})
                              
        

def extendsubscription(request):
       user_id=request.session.get('user_id')
       user=User.objects.get(id=user_id)
       user_name=user.name
       user_subscription = Subscription.objects.filter(user=user).order_by('planname').first()
       return render(request,'extendedsubscription_dealer.html',{'user_subscription':user_subscription,'user_name':user_name})



def freeplan(request):          
        user=request.session.get('user_id')
        planname='free'
        amount=0
        date=datetime.now().date()
        existing_subscription = Subscription.objects.filter(user_id=user, planname=planname).first()

        if not existing_subscription:
                current_date = datetime.now().date()
                expiry_date = current_date + timedelta(days=3)  
                new_subscription = Subscription(planname=planname, user_id=user, amount=amount, date=date,expiry_date=expiry_date)
                new_subscription.save()
        else:
                try:
                        user_id = request.session.get('user_id')
                        profile = User.objects.get(id=user_id)
                        profilepic = None
                        subscription=Subscription.objects.filter(user=profile) 
                        profilepic=DealerProfilepic.objects.get(user=profile)       
                        print('hi',subscription)
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
                except Subscription.DoesNotExist:
                        user_id = request.session.get('user_id')
                        profile = User.objects.get(id=user_id)
                        profilepic = None
                        profilepic=DealerProfilepic.objects.get(user=profile)
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
                except DealerProfilepic.DoesNotExist:
                        user_id = request.session.get('user_id')
                        profile = User.objects.get(id=user_id)
                        profilepic = None
                        subscription=Subscription.objects.filter(user=profile)
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'profilepic':profilepic,'subscription':subscription})
        return render(request,'subscription_dealer.html')        




def basicplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'basicplan_dealer.html',{'payment':payment})

def standardplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'standardplan_dealer.html',{'payment':payment})         

def premiumplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'premiumplan_dealer.html',{'payment':payment})


def success(request,payment_id,order_id,signature,plan):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    subscription=Subscription.objects.filter(user=user)
    if subscription:
           if plan=='basic':
                sub=Subscription.objects.filter(user=user).order_by('-expiry_date').first()
                date=sub.expiry_date
                expiry_date=date+timedelta(days=30)
                Subscription.objects.create(user=user,planname='basic',expiry_date=expiry_date,date=date,amount=499,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
           if plan=='standard':
                sub=Subscription.objects.filter(user=user).order_by('-expiry_date').first()
                date=sub.expiry_date
                expiry_date=date+timedelta(days=30)
                Subscription.objects.create(user=user,planname='standard',expiry_date=expiry_date,date=date,amount=999,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
           if plan=='premium':
                sub=Subscription.objects.filter(user=user).order_by('-expiry_date').first()
                date=sub.expiry_date
                expiry_date=date+timedelta(days=30)
                Subscription.objects.create(user=user,planname='premium',expiry_date=expiry_date,date=date,amount=1499,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
    else:
                if plan=='basic':
                        date=datetime.now()
                        expiry_date=date+timedelta(days=30)
                        Subscription.objects.create(user=user,planname='basic',expiry_date=expiry_date,date=date,amount=499,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
                if plan=='standard':
                        date=datetime.now()
                        expiry_date=date+timedelta(days=30)
                        Subscription.objects.create(user=user,planname='standard',expiry_date=expiry_date,date=date,amount=999,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
                if plan=='premium':
                        date=datetime.now()
                        expiry_date=date+timedelta(days=30)
                        Subscription.objects.create(user=user,planname='premium',expiry_date=expiry_date,date=date,amount=1499,razor_pay_order_id=order_id,razorpay_payment_id=payment_id,razorpay_signature=signature,paid=True)
    return redirect('dealersprofile')

def sales(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'sales_dealer.html',{'user_name':user_name})



def productslist(request,fruit):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        #fruit_data = get_list_or_404(Product, product_name=fruit)
        return render(request, 'productslist_dealer.html', {'fruit': fruit,'user_name':user_name}) #'fruit_data': fruit_data, 