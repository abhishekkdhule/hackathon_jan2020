from django.shortcuts import render,redirect
from .models import * 
from .forms import *
from faculty.models import *
from faculty.forms import *
# Create your views here.
def student_login_view(request):

    std_login=Student_login_form()
    context={
        'std_login':std_login
    }
    if request.method=="POST":
        std_login=Student_login_form(request.POST)
        std_id=request.POST.get('std_id')
        std_password=request.POST.get('std_password')
        if Students_profile_model.objects.filter(std_id=std_id).exists() and Students_profile_model.objects.filter(std_password=std_password).exists():  
            return redirect('student_profile',std_id)

    return render(request,'student1/student_login_display.html',context)

def student_profile_display(request,std_id):
    obj=Students_profile_model.objects.get(std_id=std_id)
    #fac_obj=Faculty_profile_model.objects.all()
    std_att_obj=Student_attendance_model.objects.get(std_id=std_id)
    i=0
    list=[]
    while i<6:
        fac_obj=Faculty_profile_model.objects.get(id=i+1)
        list.append(int(fac_obj.total_lecures))
        i=i+1

    print(list)
    i=0
    list1=[0,0,0,0,0,0]
    while i<6 and list[i]>0:
        list1.insert(i,(int(((std_att_obj.subject1)/list[i])*100)))
        i=i+1

    
    context={
        'std_profile_obj':obj,
        'fac_obj':list, 
        'list1':list1,  
    }
    return render(request,'student1/student_profile_display.html',context)