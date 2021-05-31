from django.shortcuts import render,redirect
from django.http import HttpResponse

def homepage(request):
    if "managerid" in request.session:
        return render(request,"TurfManager/Homepage.html",{})
    else:
        return HttpResponse("Please Login")

def ManagerProfile(request):
    pass

def ManagerLogout(request):
    try:
        if "managerid" in request.session:
            del request.session['ownerid']
        if  "managername"  in request.session:
            del request.session["ownername"]
    except KeyError:
        pass    
    return redirect("/accounts/login/")
