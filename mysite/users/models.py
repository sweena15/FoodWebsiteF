from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    MY_CHOICES = {
        ('rest', 'rest'),
        ('cust', 'cust'),
        ('admin', 'admin'),
        
    }
    
    user_type = models.CharField(max_length=50, choices = MY_CHOICES)
    

    def __str__(self):
        return str(self.user)


class CustCart(models.Model):

    cart_id = models.AutoField(primary_key=True)
    prod_code = models.IntegerField()
    quantity = models.IntegerField(default=1)
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(
            (
                str(self.cart_id),
                str(self.prod_code),
                str(self.quantity),
                str(self.username)
            )
        )


class CustRatingFeedback(models.Model):
    prod_code = models.IntegerField(default=1)
    ratings = models.FloatField()
    feedback = models.CharField(max_length=200)
    username  = models.CharField(max_length=200, default='username')
   
    def __str__(self):
        return str(
            (
                str(self.prod_code),
                str(self.ratings),
                str(self.feedback),
                str(self.username),
                
            )
        )
    
class PlacedOrders(models.Model):
    order_id = models.IntegerField()
    prod_code = models.IntegerField()
    quantity = models.IntegerField()
    user = models.CharField(max_length=200)

    def __str__(self):
        return str(
            (
                self.id,
                self.order_id,
                self.prod_code,
                self.quantity,
                self.user
            )
        )


