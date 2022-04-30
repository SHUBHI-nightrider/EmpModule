from django.shortcuts import render, HttpResponseRedirect
from .forms import EmpRegistration
from .models import User

# Create your views
#this function help to update the data of Employe registaration

def add_show(request):
    if request.method == 'POST':
        fm = EmpRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, email=em, address=ad)
            reg.save()
            fm = EmpRegistration()
    else:
        fm = EmpRegistration(request.POST)
    stud = User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm ,'stu':stud})
#this function update the data

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm =EmpRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm =EmpRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})


    #this function help to delete

def delete_data(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
