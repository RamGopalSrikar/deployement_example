from django.shortcuts import render
from django.http import HttpResponse
from user_details.models import userdetails

def index(response):
    list_name=userdetails.objects.order_by('first_name')
    dict_name={'names':list_name}
    return render(response,'user_details/index.html',context=dict_name)

# Create your views here.
