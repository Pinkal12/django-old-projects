from django.shortcuts import render
from .models import Account

# Create your views here.

def index(request):
    if request.method == "POST":
        # #way to get fporm field data
        name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['pwd']
        obj = Account(name=name,email=email,password=password)
        obj.save()
        obj_cont = Account.objects.all()
        return render(request,'account/login.html',{'obj':obj_cont})