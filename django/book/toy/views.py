from django.shortcuts import render,redirect
from django.http import HttpResponse

from toy.models import usr
from toy.models import usrs
from toy.models import contact
from toy.forms import EmpForm
from toy.forms import EmpForms

# from toy.models import Chk


def registration(request):
    return render(request,'form.html')
    
    
def reg(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            try:
               
              
                
                form.save()
                return redirect('/signin')
            except:
                pass
        else:
            form=EmpForm
            return render(request,'form.html',{'form':form})

def show(request):
    e=usr.objects.all()
    return render(request,'show.html',{'op':e})
    
def delete(request,id):
    u=usr.objects.get(id=id)
    u.delete()
    return redirect('../show')

def edit(request,id):
    u=usr.objects.get(id=id)
    return render(request,'edit.html',{'f':u})


def edcode(request,id):
    t=usr.objects.get(id=id)
    form=EmpForm(request.POST,instance=t)
    if form.is_valid():
        form.save()
        return redirect('../show')
    return render(request,'edit.html',{'f':t})

def login(request):
    return render(request,'login.html')

def logcode(request):
    if request.method=="POST":
        email=request.POST['email']
        pwd=request.POST['pwd']
        

        try:

            t=usr.objects.get(email=email)
            c=usr.objects.get(pwd=pwd)
            
            if t and c is not None:
                m=usr.objects.all()

                
                return render(request,'welcome.html',{'n':m})

            else:
                return render(request,'login.html')

           
        except:
            return render(request,'login.html')


def form(request):
    return render(request,'form.html')
def indexhome(request):
    return render(request,'indexhome.html')




# 2nd db
def regs(request):
    if request.method=="POST":
        form=EmpForms(request.POST)
        if form.is_valid():
            try:
               
              
                
                form.save()
                return redirect('/registrations')
            except:
                pass
        else:
            form=EmpForms
            return render(request,'forms.html',{'form':form})



def registrations(request):
    return render(request,'forms.html')

def shows(request):
    e=usrs.objects.all()
    return render(request,'shows.html',{'op':e})


    # places

def international(request):
    return render(request,'places_international.html') 

def indian(request):
    return render(request,'places_india.html')



# crud

def deletes(request,id):
    u=usrs.objects.get(id=id)
    u.delete()
    return redirect('../shows')

def edits(request,id):
    u=usrs.objects.get(id=id)
    return render(request,'edits.html',{'f':u})


def edcodes(request,id):
    t=usrs.objects.get(id=id)
    form=EmpForms(request.POST,instance=t)
    if form.is_valid():
        form.save()
        return redirect('../shows')
    return render(request,'edits.html',{'f':t})



# 3rd



# Create your views here.
def index(request):
    if request.method=="POST":
       
        name = request.POST.get('name', '')
        persons = request.POST.get('persons', '')
        days = request.POST.get('days', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        if name and persons and days and  email:
            c=contact(name=name,persons=persons,days=days,phone=phone,email=email)
            c.save()
        else:
            return HttpResponse("enter the details")
    return render(request,'bookeddtls.html')


def output(request):
    all_name=contact.objects.all()
    return render(request,"bookedfetch.html",{'names':all_name})
def booked(request):
    return render(request,'bookeddtls.html')








# chk

def test(request):
    return render(request,'Admina.html')


# Create your views here.

def admina(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pswd=request.POST['pswd']

        try:
            if uname=="admin" and pswd=="admin":
                return redirect('/show')
            else:
                return HttpResponse("invalid id and pass")
        except:
            return HttpResponse("failed")
    else:
        return HttpResponse("all ok")


def trip(request):
    return render(request,'trip.html')