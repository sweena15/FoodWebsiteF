from django.shortcuts import *
from users.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from users.models import Profile, CustCart, PlacedOrders
from django.http import JsonResponse
import json

# Create your views here.
#----------------------------------------------------------------------------------------------







# Function based Register View
#----------------------------------------------------------------------------------------------
def Register(request):

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(username)
            print(password1)
            print(password2)
            id = form.instance.id
            return redirect('users:profformcreate', userid = id)

        
        
        else:

            
            username = form.data.get('username')
            user_exists = User.objects.filter(username=username).exists()
            password1 = form.data.get('password1')
            password2 = form.data.get('password2')
            
            if user_exists:
                    messages.success(
                    request,
                    'Username already exists'
                   )

            elif password1 != password2:
                    messages.success(
                    request,
                    'Password does not match'
                   )

            elif len(password1)<8:
                    messages.success(
                    request,
                    'password length cannot be less than 8'
                   )

            
        
            print('username = ',username)
            print('password1 = ',password1)
            print('password2 = ',password2)
                  
            return redirect('register')
    
    context={
        'form':form
        }

    return render(request, 'users/register.html', context)
#----------------------------------------------------------------------------------------------







# Function based Login_view View
#----------------------------------------------------------------------------------------------
def Login_view(request):

    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            messages.success(
                request,
                'Username or Password is not valid'
            )
            return redirect('login')

        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Admin {}, you have been successfully logged in'.format(username)
            )
            return redirect('food:Index')

        elif user is not None:
            login(request, user)
            messages.success(
                request,
                '{}, you have been successfully logged in'.format(username)
            )
            return redirect('food:Index')

            
        
        
    context = {

        }
    return render(request, 'users/login.html', context)
#----------------------------------------------------------------------------------------------







# Function based logout_view View
#----------------------------------------------------------------------------------------------
def logout_view(request):
    

    if request.method == 'POST':
        logout(request)
        messages.success(
            request,
            'You have been logged out'
        )
        return redirect('food:Index')

    return render(request, 'users/logout.html')
#----------------------------------------------------------------------------------------------







# Function based ProfileView View
#----------------------------------------------------------------------------------------------
def ProfileView(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    context ={
        }


    return render(request,'users/profile.html', context)
#----------------------------------------------------------------------------------------------







# Function based ProfileFormEdit View
#----------------------------------------------------------------------------------------------
def ProfileFormEdit(request, userid):


    prof = Profile.objects.get(user=userid)
    form = ProfileForm(request.POST or None, request.FILES or None ,instance=prof)
    
    if request.method == 'POST':
        form.save()
        return redirect('profile')

    
    context = {
        'userid':userid,
        'form': form
        }

    return render(request, 'users/profform.html', context)
#----------------------------------------------------------------------------------------------







# Function based ProfFormCreate View
#----------------------------------------------------------------------------------------------
def ProfFormCreate(request, userid):
    prof = Profile.objects.get(user=userid)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=prof)

    if request.method == 'POST':
        print('userid: {}'.format(userid))

        
        if form.is_valid():
            form.save()
            return redirect('login')
                

    context ={

        'userid':userid,
        'form':form
        }
    return render(request, 'users/profform.html', context)
#----------------------------------------------------------------------------------------------







# Function based Cart View
#----------------------------------------------------------------------------------------------
def CustCartView(request, itemid, pdcd, user):

    context = {
        'pdcd':pdcd,
        'user':user
    }

    if request.method == 'POST':

        ObjCustCart = CustCart(
            prod_code=pdcd,
            username=user,
            quantity=request.POST.get('qty')
        )

        ObjCustCart.save()

        return redirect('food:detail', itemid=itemid)

    return render(request, 'users/cart.html', context)
#----------------------------------------------------------------------------------------------







# Function based Cart Update View
#----------------------------------------------------------------------------------------------
def CartUpdateView(request, cartid, itemid):

    cco = CustCart.objects.get(cart_id = cartid)

    form = CustCartUpd(request.POST or None, instance=cco)

    if request.method == 'POST':
        if form.is_valid():
            
            form.save()
        
            return redirect('food:detail', itemid=itemid)
        
    
    context = {
        'cartid':cartid,
        'itemid':itemid,
        'form':form,
        }

    return render(request, 'users/cartupd.html', context)
#----------------------------------------------------------------------------------------------







# Function based Customer Feedback View
#----------------------------------------------------------------------------------------------
def CustRatFeedView(request, itemid, pc, username):

    
    form = CustRatFeedForm(request.POST or None)

    if request.method == 'POST':
        form.instance.prod_code = pc
        form.instance.username=username
        if form.is_valid():
            form.save()
            return redirect('food:detail', itemid=itemid)
        
    context = {
        'itemid':itemid,
        'pc':pc,
        'username':username,
        'form':form
        }

    return render(request, 'users/crf.html', context)
#----------------------------------------------------------------------------------------------







# Function based Csutomer Feedback Update View
#----------------------------------------------------------------------------------------------
def CustRatFeedUpdateView(request, itemid, csrfid):

    crfo = CustRatingFeedback.objects.get(pk=csrfid)
    form = CustRatFeedForm(request.POST or None, instance=crfo)


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('food:detail', itemid=itemid)
    context={
       'itemid':itemid,
        'form':form,
        'username':request.user.username,
        'csrfid':csrfid,
        }

    return render(request,'users/crf.html',context)
#----------------------------------------------------------------------------------------------







# Function based Csutomer Feedback Delete View
#----------------------------------------------------------------------------------------------
def CustRatFeedDeleteView(request, itemid, csrfid):

    crfo = CustRatingFeedback.objects.get(pk=csrfid)
   


    if request.method == 'POST':
        crfo.delete()
        return redirect('food:detail', itemid=itemid)
    
    context={
        'itemid':itemid,
        'crfo':crfo
        }

    return render(request,'users/crf_del.html',context)

def Payment(request, amt, qnt, cartid, itemid):
    print(request, amt, qnt, cartid, itemid)
    context={
        'amt':amt,
        'qnt':qnt,
        'tot':amt*qnt,
        'cartid':cartid,
        'itemid':itemid
    }
    return render(request, 'users/payment.html', context)


def OnApprove(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)

        context = {

        }

        return JsonResponse(context)


def PaymentSuccess(request, cartid, itemid):
    print(cartid, itemid)

    coo=CustCart.objects.get(cart_id=cartid)

    opo = PlacedOrders(
        order_id=coo.cart_id, 
        prod_code=coo.prod_code,
        quantity=coo.quantity,
        user=coo.username
        )

    opo.save()
    coo.delete()

    context={
        'cartid':cartid,
        'itemid':itemid
    }

    return render(request, 'users/pymtsuccess.html', context)


def PlacedOrdersView(request):
    
    username = request.user.username
    opo = PlacedOrders.objects.filter(user=username)
    
    context = {
        'opo':opo
    }
    
    return render(request, 'users/placedorders.html', context)













