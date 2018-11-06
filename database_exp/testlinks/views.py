from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testlinks/index.html')

def others(request):
    return render(request,'testlinks/others.html')

def rellinks(request):
    return render(request,'testlinks/rellinks.html')
