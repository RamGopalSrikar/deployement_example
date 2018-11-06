from django.shortcuts import render
from logindetails.form import FormName

# Create your views here.
def index(request):
    form=FormName()
    if request.method=='POST':
        form=FormName(request.POST)
        if form.is_valid():

            form.save()
            print("name :"+ form.cleaned_data['name'])
            print('yoyo')

        else:
            print('form invalid')



    print('hello world')
    return render(request,'logindetails/formname.html',{'form':form})
