from .models import Stock,Category
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

        labels={
            'password1': 'Password',
            'password2':'Confirm password'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category','item_name','quantity']


    def clean_item_name(self):
        item_name=self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name


class StockSearchForm(forms.ModelForm):
    #the export to csv line below gives a check box in the fronend that when checked exports the stock_list to CSV
    export_to_CSV=forms.BooleanField(required=False)
    class Meta:
        model=Stock
        fields=['category','item_name']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name','quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['issue_quantity', 'issue_by']

class ReceiveForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['receive_quantity','receive_by']

class ReorderForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['reorder_level']
