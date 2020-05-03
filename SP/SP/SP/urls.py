"""SP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main.views import home,train,predict,add,training,prediction,clear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('Home.html',home,name='home'),
    path('Train.html',train,name='train'),
    path('Predict.html',predict,name='predict'),
    path('Add.html',add,name='add'),
    path('Training.html',training,name='training'),
    path('Prediction.html',prediction,name='prediction'),
    path('Clear.html',clear,name='prediction'),
]