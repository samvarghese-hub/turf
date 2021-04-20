from django.shortcuts import render
from django.http import HttpResponse

def Addition(request):
    if request.method=="POST":
        num1=int(request.POST.get("txtNumber1"))
        num2=int(request.POST.get("txtNumber2"))
        if(request.POST.get("button1")):
            sum=num1+num2
            return render(
                request,
                "user/Addition.html",
                {
                    "number1":num1,
                    "number2":num2,
                    "Result":sum
                })
        elif(request.POST.get("button2")):
            sub=num1-num2
            return render(
                request,
                "user/Addition.html",
                {
                    "number1":num1,
                    "number2":num2,
                    "Result":sub
                })
            
    else:
        return render(request,"user/Addition.html",{})

