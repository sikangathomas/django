from django.contrib import admin
from .models import Stock,Category,Profile
from .forms import StockCreateForm,CategoryForm

class CategoryCreateAdmin(admin.ModelAdmin):
   list_display = ['name']
   form = CategoryForm
   search_fields = ['name']

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category','item_name','issue_by','receive_by','quantity']
    form = StockCreateForm
    search_fields = ['item_name']
    list_filter = ['category']

#Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(Profile)
