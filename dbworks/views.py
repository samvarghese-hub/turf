from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import District


def ManageStudents(request):
    Data=Student.objects.all() #Fetch all Datas
    
    if request.method=='POST':
        objStudent=Student(name=request.POST.get("txtStudentName"),rollno=request.POST.get("txtRollNo"))
        objStudent.save() 
        
        return render(request,"dbworks/StudentData.html",{"StudentDatas":Data})

    else:
       
        return render(request,"dbworks/StudentData.html",{"StudentDatas":Data})

def Managedist(request):
    Dis=District.objects.all()
    # print(Dis)
    if request.method=='POST':
        objdis=District(dist=request.POST.get("txtdist"),names=request.POST.get("txtname"))
        objdis.save() 
        return render(request,"dbworks/Districtdata.html",{"Distdata":Dis})
    else:
       
        return render(request,"dbworks/Districtdata.html",{"Distdata":Dis})

def DeleteDistrict(request,id):
    DeleteDis=District.objects.get(id=id)
    DeleteDis.delete()
    return render(request,"dbworks/Districtdata.html",{})





# #Fetch all Datas 
# >>> StudentData=Student.objects.all()
# >>> for data in StudentData: 
# >>>     print(data.name)
