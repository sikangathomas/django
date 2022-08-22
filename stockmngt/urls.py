"""stockmngt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stockmanagement import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup',views.signup,name='signup'),
    path('stocklist', views.stock, name='stocklist'),
    path('stock-export', views.stockexport, name='stock-export'),
    path('history', views.stockhistory, name='history'),
    path('export-history', views.exporthistory, name='export-history'),
    path('add_stock', views.createstock, name='add-stock'),
    path('update/<str:pk>/',views.updatestock,name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('item-details/<str:pk>/', views.itemdetail, name='item-detail'),
    path('issue-item/<str:pk>/', views.IssueItem, name='issue-item'),
    path('receive-item/<str:pk>/', views.receiveItem, name='receive-item'),
    path('reorder_level/<str:pk>/', views.reoderLevel, name='reorder-level'),
    path('login',auth_views.LoginView.as_view(template_name='dashboard/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)