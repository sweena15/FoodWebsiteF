from django.contrib import admin
from food.models import History, Item
# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'rest_owner')

admin.site.register(Item, ItemAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('username', 'prod_code', 'item_name', 'operation')

admin.site.register(History, HistoryAdmin)