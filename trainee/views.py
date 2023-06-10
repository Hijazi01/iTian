from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def Tlist(req):
    context = {}
    context['tl'] = Mytrainee.objects.all()
    return render(req,'student/liststudent.html', context)
def TUpdate(req,ID):
    context = {}
    T=Mytrainee.objects.get(id=ID)
    context['tup']=T
    if(req.method=="POST"):
        Mytrainee.objects.filter(id=ID).update(name=req.POST['name'], age=req.POST['age'], email=req.POST['email'], faculty=req.POST['faculty'], appreciation=req.POST['appreciation'])
        return HttpResponseRedirect('/trainee')
    return render(req,'student/update.html', context)
def TDelete(req,ID):
    Mytrainee.objects.filter(id=ID).delete()
    return HttpResponseRedirect('/trainee')
def Tadd(req):
    if (req.method == 'POST'):
        Mytrainee.objects.create(name=req.POST['name'], age=req.POST['age'], email=req.POST['email'], faculty=req.POST['faculty'], appreciation=req.POST['appreciation'])
        return HttpResponseRedirect('/trainee')
    else:
        return render(req, 'student/add.html')