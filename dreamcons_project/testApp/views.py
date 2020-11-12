from django.shortcuts import render
from django.http import HttpResponse
from .models import Person,Group,Membership
from .import views

# Create your views here
def home(request):
    persons=Person.objects.all()
    groups=Group.objects.all()
    members=Membership.objects.all()
    return render(request,"index.html",locals())
    #return HttpResponse("Allah Almighty Is Greatest Of All")

def param(request,pk):
    print("pk : ",pk)
    return HttpResponse("Your Primary Key is : {0}".format(pk)) 

def regular_param(request,pk):
    return HttpResponse("Your Response Primary Key is : {0}".format(pk)) 

def create_developer(request):
    if(request.POST):
        print("Method : true")
    return render(request,'create_developer.html',locals())