from django.urls import path
from testlinks import views

app_name='testlinks'

urlpatterns=[
    path('others/',views.others,name='others'),
    path('rellinks/',views.rellinks,name='rellinks'),
]
