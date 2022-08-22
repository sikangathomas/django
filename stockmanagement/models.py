from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
#making choices
category_choice=(
    ('Phones', 'Phones'),
    ('Nails','Nails'),
    ('Electronics','Electronics'),
    ('Clothing','Clothing'),
)
#creasting a model that we use to make user be able to create item choices in frontend

class Category(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    receive_quantity=models.IntegerField(default='0',blank=True,null=True)
    receive_by=models.CharField(max_length=50,blank=True,null=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issued_to=models.CharField(max_length=50,blank=True,null=True)
    phone_number=models.CharField(max_length=50,blank=True,null=True)
    created_by=models.CharField(max_length=50,blank=True,null=True)
    reorder_level=models.IntegerField(default='0',blank=True,null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.item_name+ " "+str(self.quantity)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.item_name)
        super().save(*args, **kwargs)

class StockHistory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    receive_quantity=models.IntegerField(default='0',blank=True,null=True)
    receive_by=models.CharField(max_length=50,blank=True,null=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issued_to=models.CharField(max_length=50,blank=True,null=True)
    phone_number=models.CharField(max_length=50,blank=True,null=True)
    created_by=models.CharField(max_length=50,blank=True,null=True)
    reorder_level=models.IntegerField(default='0',blank=True,null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=False)
    slug = models.SlugField(null=True, blank=True)






