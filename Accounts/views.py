from django.shortcuts import render,redirect,get_object_or_404
from . models import TurfOwnerRegistration
from MasterEntry.models import District
from TurfOwner.models import TurfManagerRegistration
from django.http import HttpResponse 
from django.contrib import messages

def selectAllDistrict():
    DistrictRecords=District.objects.all()
    return DistrictRecords


# Create your views here.
def OwnerRegistration(request):
    DistrictRecords=selectAllDistrict()
    if request.method=="POST":
        ownerobj=TurfOwnerRegistration()
        ownerobj.turfowner_name=request.POST.get("txtname")
        ownerobj.turfowner_contact=request.POST.get("txtcontact")
        ownerobj.turfowner_email=request.POST.get("txtemail")
        ownerobj.turfowner_gender=request.POST.get("rdbGender")
        ownerobj.turfowner_address=request.POST.get("txtAddress")
        ownerobj.turfowner_image=request.FILES.get("fileImage")
        ownerobj.turfowner_username=request.POST.get("txtUsername")
        ownerobj.turfowner_password=request.POST.get("txtPassword")
        # Foreign Key Save Concept
        DistrictObj=District.objects.get(id=request.POST.get("slctDistrict"))
        ownerobj.turfowner_district=DistrictObj

        ownerobj.save()
        # return render(request,"Accounts/TurfOwnerRegistration.html",{"DistrictRecordSets":DistrictRecords})
        messages.success(request, 'created successfully.')
      

        return render(request,"Accounts/TurfOwnerRegistration.html",{"DistrictRecordSets":DistrictRecords})  
    else:
         return render(request,"Accounts/TurfOwnerRegistration.html",{"DistrictRecordSets":DistrictRecords})


def login(request):
    if request.method=='POST':
        turfOwnerDataCount=TurfOwnerRegistration.objects.filter(turfowner_username=request.POST.get("txtUsername"),turfowner_password=request.POST.get("txtPassword")).count()
        turfManagerDataCount=TurfManagerRegistration.objects.filter(turfManager_username=request.POST.get("txtUsername"),turfManager_password=request.POST.get("txtPassword")).count()
        
        
        if turfOwnerDataCount>0:
            turfOwnerobj = get_object_or_404(TurfOwnerRegistration, turfowner_username=request.POST.get("txtUsername"),turfowner_password=request.POST.get("txtPassword"))
            request.session["ownerid"]=turfOwnerobj.id
            request.session["ownername"]=turfOwnerobj.turfowner_name
            return redirect("/turfowner/homepage/")
        
        elif turfManagerDataCount>0:
            turfManagerobj = get_object_or_404(TurfManagerRegistration, turfManager_username=request.POST.get("txtUsername"),turfManager_password=request.POST.get("txtPassword"))
            request.session["managerid"]=turfManagerobj.id
            request.session["managername"]=turfManagerobj.turfManager_name
            return redirect("/turfmanager/homepage/")
        else: 
            return HttpResponse("Invalid Data")
    return render(request,"Accounts/Login.html",{})

    

    
 
   
