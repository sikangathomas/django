from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
import csv
from .models import Stock,StockHistory
from .forms import StockCreateForm, StockSearchForm,StockUpdateForm,IssueForm,ReceiveForm,ReorderForm,SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    registered = False
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'dashboard/signup.html', {'form': form})

def home(request):
    title="Home"
    description="This is our home page"
    context={
        "title":title,
        "description":description
    }
    return render(request,'home.html',context)

@login_required
def stock(request):
    list=Stock.objects.all()

    context={
        'itemlist':"ITEM LIST",
        'stocklist': list
    }
    return render(request,'list.html',context)

def stockexport(request):
    queryset=Stock.objects.all()
    response=HttpResponse('text.csv')
    response['Content-Disposition']='attachment; filename=StockList.csv'
    writer=csv.writer(response)
    writer.writerow(['CATEGORY', 'ITEM NAME','QUANTITY'])
    stocklist=queryset.values_list('category','item_name','quantity')
    writer.writerow(stocklist)
    return response

def createstock(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Item added successfully on the stock")
        return redirect('stocklist')
    context={
        'form':form,
        'title':"Add Stock"
    }
    return render(request,'add_stock.html',context)

def updatestock(request,pk):
    queryset=Stock.objects.get(id=pk)
    form=StockUpdateForm(instance=queryset)
    if request.method=='POST':
        form=StockUpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully")
        return redirect('stocklist')

    context={
        'form': form
    }
    return render(request,'add_stock.html',context)

def delete(request,pk):
    queryset=Stock.objects.get(id=pk)
    if request.method=="POST":
        queryset.delete()
        messages.success(request, "Item deleted successfully")
        return redirect('stocklist')
    return render(request,'delete.html')

def itemdetail(request,pk):
    queryset=Stock.objects.get(id=pk)
    context={
        'title':queryset.item_name,
        'queryset':queryset
    }
    return render(request,'itemdetail.html',context)

def IssueItem(request,pk):
    queryset=Stock.objects.get(id=pk)
    form=IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.receive_quantity=0
        if instance.issue_quantity<=instance.quantity:
         instance.quantity=instance.quantity-instance.issue_quantity
         instance.issue_by=str(request.user)
         instance.save()
         messages.success(request, str(instance.issue_quantity)+' has been issued from '+ str(instance.item_name))
        else:
            messages.success(request, 'The ' +str(instance.item_name) +' to be issued exceeds those in the stock')

        return redirect('stocklist')
    context={
        'title':'Issue' +str(queryset.item_name),
        'queryste':queryset,
        'form':form,
        'username':'Issued by ' +str(request.user)
    }
    return render(request,'add_stock.html',context)

def receiveItem(request,pk):
    queryset=Stock.objects.get(id=pk)
    form=ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.issue_quantity=0
        instance.quantity+=instance.receive_quantity
        instance.receive_by = str(request.user)
        instance.save()
        messages.success(request, str(instance.receive_quantity)+ ' '+ str(instance.item_name)+' ' ' added to stock successfuly' )

        return redirect('stocklist')
    context={
        'title':'Receive'+str(queryset.item_name),
        'queryset':queryset,
        'form':form
    }
    return render(request,'add_stock.html',context)

def reoderLevel(request,pk):
    queryset=Stock.objects.get(id=pk)
    form=ReorderForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,str(instance.item_name)+'  reorder level set to '+str(instance.reorder_level))
        return redirect('stocklist')
    context={
        'queryste':queryset,
        'form':form
    }
    return render(request,'add_stock.html',context)

@login_required
def stockhistory(request):
    queryset=StockHistory.objects.all()
    context={
        'title':'STOCK HISTORY',
        'queryset':queryset
    }
    return render(request,'history.html',context)

@login_required
def exporthistory(request):
    queryset=StockHistory.objects.all()
    responce = HttpResponse('text/csv')
    responce['Content-Disposition'] = 'attachment; filename=stock-history.csv'
    writer = csv.writer(responce)
    writer.writerow(
        ['Item Name', 'Quantity', 'Issue Quantity', 'Issue By', 'Receive Quantity', 'Receive By', 'Last Updated'])
    history = queryset.values_list('item_name', 'quantity', 'issue_quantity', 'issue_by', 'receive_quantity',
                                   'receive_by', 'last_updated')
    for historydata in history:
        writer.writerow(historydata)
    return responce



