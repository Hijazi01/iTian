from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def Tlist(req):
    context = {}
    context['tl'] = Mytrainee.objects.all()
    return render(req,'student/liststudent.html', context)
def TUpdate(req):

    return HttpResponse('update')
def TDelete(req,ID):
    Mytrainee.objects.filter(id=ID).delete()
    return HttpResponseRedirect('/trainee')
def Tadd(req):
    if (req.method == 'POST'):
        Mytrainee.objects.create(name=req.POST['name'], age=req.POST['age'], email=req.POST['email'], Faculty=req.POST['Faculty'], appreciation=req.POST['appreciation'])
        return redirect('/')
    else:
        return render(req, 'student/add.html')