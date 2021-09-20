from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
globalcount = dict()
arr=['Java','Python','C++','C','JavaScript','PHP','SQL']
# Create your views here.
def start(request):
    dic={"arr":arr}
    return render(request,'votingapp/index.html',context=dic)

def getQuery(request):
    q=request.GET['language']
    if q in globalcount:
        globalcount[q]=globalcount[q]+1
    elif q in arr:
        globalcount[q]=1
    dic={
        "arr":arr,
        "globalcount":globalcount
    }
    return render(request,'votingapp/index.html',context=dic)

def sort(request):
    global globalcount
    globalcount= dict(sorted(globalcount.items(),key=lambda x:x[1],reverse=True))
    dic={
        "arr":arr,
        "globalcount":globalcount
    }
    return render(request,'votingapp/index.html',context=dic)
