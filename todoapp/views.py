from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
# Create your views here.

def start(request):
    return render(request,'todoapp/index.html')
def submit(request):
    obj=Todo()
    obj.title=request.GET['title']
    obj.desc=request.GET['desc']
    obj.num=request.GET['num']
    obj.save()
    dic={ "alltodos":Todo.objects.all()
    }
    return render(request,'todoapp/list.html',context=dic)
def delete(request,id):
    obj=Todo.objects.get(id=id)
    obj.delete()
    dic={ "alltodos":Todo.objects.all()
    }
    return render(request,'todoapp/list.html',context=dic)

def list(request):
    dic={ "alltodos":Todo.objects.all()
    }
    return render(request,'todoapp/list.html',context=dic)

def sortdata(request):
    dic={ "alltodos":Todo.objects.all().order_by('num')
    }
    return render(request,'todoapp/list.html',context=dic)

def search(request):
    q=request.GET['search']
    dic={
        "alltodos": Todo.objects.filter(title__contains=q)
    }
    return render(request,'todoapp/list.html',context=dic)
def edit(request,id):
    obj=Todo.objects.get(id=id)
    dic={
    "title":obj.title,
    "desc":obj.desc,
    "num":obj.num,
    "id":obj.id
    }
    return render(request,'todoapp/edit.html',context=dic)

def update(request,id):
    obj=Todo(id=id)
    obj.title=request.GET['title']
    obj.desc=request.GET['desc']
    obj.num=request.GET['num']
    import datetime
    update=datetime.datetime.now()
    obj.create=update
    obj.save()
    dic={ "alltodos":Todo.objects.all()
    }
    return render(request,'todoapp/list.html',context=dic)
