from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from myaccounts.models import *
def login(req):
    context={}
    if(req.method=="POST"):
        U = MyUser.objects.filter(username=req.POST['username'],password=req.POST['password'])
        if(len(U)!=0):
            req.session["username"]=U[0].username
            return HttpResponseRedirect('/trainee')
        else:
             context['msg']='invalid email or password'
    return render(req,'myaccount/login.html',context=context)
def registration(req):
    if(req.method=='POST'):
        MyUser.objects.create(username=req.POST['username'],password=req.POST['password'],email=req.POST['email'])
        return redirect('myaccount/login.html')
    return render(req, 'myaccount/profile.html')
def logout(req):
    req.session.clear()
    return render(req, 'myaccount/logout.html')

def all_list(req):
    return render(req,'page_all_list.html')

def profile(req):
    return render(req,'profile.html')