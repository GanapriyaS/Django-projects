from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def start(request):
    return render(request,'calculator/index.html')
def calc(request):
    q=request.GET['query']
    # jsondic={"q":q}
    # return JsonResponse({"q":"q"})
    try:
        ans=eval(q)
        dic={ "q":q,
              "ans":ans,
              "error":False,
              "result":True
        }
        return render(request,'calculator/index.html',context=dic)
    except:
        dic={
              "error":True,
              "result":False
        }
        return render(request,'calculator/index.html',context=dic)
   
