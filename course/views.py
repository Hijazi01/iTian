from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def Clist(req):
    context={}
    context['cl']=Course.objects.all()
    return render(req, 'courses/listcoures.html',context)
def Cadd(req):
     if (req.method=='POST'):
         Course.objects.create(name=req.POST['name'],duration=req.POST['duration'],details=req.POST['details'])
         return redirect('/course')
     else:
         return render(req,'courses/add.html')

def Cdelete(req,ID):
    Course.objects.filter(id=ID).delete()
    return HttpResponseRedirect('/course')
def Cupdate(req,ID):
    context = {}
    C = Course.objects.get(id=ID)
    context['cup'] = C
    if (req.method == "POST"):
        Course.objects.filter(id=ID).update(name=req.POST['name'], age=req.POST['age'], email=req.POST['email'],faculty=req.POST['faculty'], appreciation=req.POST['appreciation'])
        return HttpResponseRedirect('courses/')
    return render(req,'courses/update.html', context)
