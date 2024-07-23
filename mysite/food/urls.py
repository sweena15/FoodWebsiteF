from django.urls import path
from food import views
app_name = 'food'

urlpatterns = [
    
    #----------------------------------------------------------------------------------------------
    # Function based Index view
    path('home/', views.Index, name ='Index'),
    #----------------------------------------------------------------------------------------------
    # Class based Index view
    # path("home/", views.IndexClassView.as_view(), name="Index"),

    



    #----------------------------------------------------------------------------------------------
    # Function based Detail view
    path('detail/<int:itemid>/', views.Detail, name ='detail'),
    #----------------------------------------------------------------------------------------------
    # Class based Detail view
    #path('detail/<int:pk>/', views.DetailClassView.as_view(), name ='detail'),

    



    #----------------------------------------------------------------------------------------------
    # Function based CreateItem view
    #path("add/", views.CreateItem, name="createitem"),
     #----------------------------------------------------------------------------------------------
    # Class based Detail view
    path("add/", views.IndexCreateItemView.as_view(), name="createitem"),




    
    path('update/<int:itemid>', views.UpdateItem, name='updateitem'),
    path('delete/<int:itemid>', views.DeleteItem, name='deleteitem'),
]
