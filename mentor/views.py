from django.shortcuts import render,redirect
from faculty.forms import *
from student1.models import *
# Create your views here.
def mentor_login_view(request):
    fac_login=Faculty_login_form()
    context={
        'fac_login':fac_login
    }
    if request.method=="POST":
        fac_login=Faculty_login_form(request.POST)
        fac_id=request.POST.get('fac_id')
        fac_password=request.POST.get('fac_password')
        if Faculty_profile_model.objects.filter(fac_id=fac_id).exists() and Faculty_profile_model.objects.filter(fac_password=fac_password).exists():  
            return redirect('mentor_profile',fac_id)

    return render(request,'mentor/mentor_login_display.html',context)

def mentor_profile_view(request,fac_id):
    obj_fac=Faculty_profile_model.objects.get(fac_id=fac_id)
    obj_std= Students_profile_model.objects.all()[:4]
    # if fac_id == 1111:
    #     obj_std=Students_profile_model.objects.all()[:4]
    # if fac_id == 3333:
    #     obj_std=Students_profile_model.objects.all()[4:8]
    # lecture=Faculty_profile_model(fac_id=)
    
    context={
        'fac_profile_obj':obj_fac,
        'obj_std':obj_std,
     #   'lecture':lecture,
       
    }
    return render(request,'mentor/mentors_profile_display.html',context)
