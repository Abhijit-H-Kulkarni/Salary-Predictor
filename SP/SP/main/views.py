from django.shortcuts import render
from .models import Data
from sklearn.linear_model import LinearRegression

X = []
Y = []
model = LinearRegression()

def home(request):
   return render(request, "Home.html", {})

def train(request):
   return render(request, "Train.html", {})

def predict(request):
   return render(request, "Predict.html", {})

def add(request):
   if request.method == 'POST':
      data = Data()
      data.exp = request.POST.get('Experience')
      data.sal = request.POST.get('Salary')
      data.save()
      return render(request, 'Train.html')  

def training(request):
   global X,Y,model
   objects = Data.objects.all()
   for obj in objects:
      X.append([obj.exp])
      Y.append(obj.sal)
   model.fit(X,Y)
   return render(request, 'Home.html')

def prediction(request):
   global X,Y,model
   objects = Data.objects.all()
   for obj in objects:
      X.append([obj.exp])
      Y.append(obj.sal)
   model.fit(X,Y)
   if request.method == 'POST':
      exp = int(request.POST.get('Experience'))
      exp_test = []
      exp_test.append([exp])
      sal = model.predict(exp_test)
   return render(request,'Predict2.html',{'sal': int(sal),'exp':exp})

def clear(request):
   if(len(Data.objects.all())>0):
      Data.objects.all().delete()
   return render(request, 'Train.html')