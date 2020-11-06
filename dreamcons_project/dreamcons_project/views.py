from django.http import HttpResponse
from .settings import STATIC_URL,STATICFILES_DIRS,BASE_DIR
from django.shortcuts import render

def home(request):
    age=20
    my_list=[1,2,3,4,5]
    print("static path  : ",STATICFILES_DIRS)
    return render(request,"home.html",locals())
    #return HttpResponse("Allah Almighty IS Greatest Of All")