from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    rest_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prod_code = models.IntegerField(default=100)
    
    added_by = models.CharField(max_length=50, default='admin')
    
    item_name = models.CharField(max_length = 50)
    item_desc = models.CharField(max_length = 500, default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis nostrum ipsam voluptatibus maiores quasi, cum ipsum sit blanditiis expedita recusandae officia quia, alias, magnam facere quidem sint quis pariatur temporibus?r')
    item_price = models.IntegerField(default=0)
    
    item_image = models.CharField(max_length = 500, default = 'https://cdn-icons-png.flaticon.com/512/1377/1377194.png')
    
    def __str__(self):
        return str(
                self.item_name
        )

class History(models.Model):

    username = models.CharField(max_length=100)
    prod_code = models.IntegerField(default=100)
    item_name  = models.CharField(max_length=200)
    operation = models.CharField(max_length=100)

    def __str__(self):
        return str(
            (
                self.prod_code,
                self.username,
                self.item_name,
                self.operation
            )
        )



        
