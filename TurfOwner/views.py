from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import TurfManagerRegistration
from MasterEntry.models import District
from Accounts.models import TurfOwnerRegistration

# Create your views here.
def selectAllDistrict():
    DistrictRecords=District.objects.all()
    return DistrictRecords

def homepage(request):
    if "ownerid" in request.session:
        return render(request,"TurfOwner/Homepage.html",{})
    else:
        return HttpResponse("Please Login")

def OwnerProfile(request):
    pass

def AddTurfManager(request):
    if "ownerid" in request.session:
        DistrictRecords=selectAllDistrict()
        if request.method=="POST":
            managerObj=TurfManagerRegistration()
            managerObj.turfManager_name=request.POST.get("txtname")
            managerObj.turfManager_contact=request.POST.get("txtcontact")
            managerObj.turfManager_email=request.POST.get("txtemail")
            managerObj.turfManager_gender=request.POST.get("rdbGender")
            managerObj.turfManager_address=request.POST.get("txtAddress")
            managerObj.turfManager_image=request.FILES.get("fileImage")
            managerObj.turfManager_username=request.POST.get("txtUsername")
            managerObj.turfManager_password=request.POST.get("txtPassword")
            # Foreign Key Save Concept
            DistrictObj=District.objects.get(id=request.POST.get("slctDistrict"))
            managerObj.turfManager_district=DistrictObj
            
            turfOwnerobj=TurfOwnerRegistration.objects.get(id=request.session["ownerid"])
            managerObj.turfManager_owner=turfOwnerobj
            managerObj.save()
            return render(request,"TurfOwner/TurfManager.html",{"DistrictRecordSets":DistrictRecords})  
        else:
            return render(request,"TurfOwner/TurfManager.html",{"DistrictRecordSets":DistrictRecords})
    else:
        return HttpResponse("Please Login")

def ownerLogout(request):
    try:
        if "ownerid" in request.session:
            del request.session['ownerid']
        if  "ownername"  in request.session:
            del request.session["ownername"]
    except KeyError:
        pass    
    return redirect("/accounts/login/")
