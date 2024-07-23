from django.urls import path, include
from users import views as userviews

app_name = 'users'


urlpatterns = [
    #profile form editing
    path('profformedit/<int:userid>/', userviews.ProfileFormEdit, name='profformedit'),
    
    #profile form creating
    path('profformcreate/<int:userid>/', userviews.ProfFormCreate, name='profformcreate'),
    
    #cart item create
    path('cart/<int:itemid>/<int:pdcd>/<str:user>/', userviews.CustCartView, name='cart'),

    #cart update
    path('cartupd/<int:cartid>/<int:itemid>/', userviews.CartUpdateView, name ='cartupd'),

    
    #customer rating-feedback 
    path('crf/<int:itemid>/<int:pc>/<str:username>/', userviews.CustRatFeedView, name='crf'),


    #customer rating-feedback update
    path('crfupd/<int:itemid>/<int:csrfid>/',userviews.CustRatFeedUpdateView, name='crfupd'),

    #customer rating-feedback delete
    path('crfdel/<int:itemid>/<int:csrfid>/',userviews.CustRatFeedDeleteView, name='crfdel'),

    path('buy/<int:amt>/<int:qnt>/<int:cartid>/<int:itemid>/', userviews.Payment, name='buy'),

     # paypal on approve
    path('oa/', userviews.OnApprove, name='oa'),

    # paypal payment success
    path('ps/<int:cartid>/<int:itemid>/', userviews.PaymentSuccess, name='ps'),

    # placed orders
    path('pldords/', userviews.PlacedOrdersView, name='pldords'),
]
