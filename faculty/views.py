from django.shortcuts import render,redirect
from .models import *
from .forms import *
from student1.models import *
from student1.models import *
from student1.forms import *

# Create your views here.
def about_us(request):
    return render(request,'faculty/about.html')

def homepage_display(request):
    return render(request,'faculty/index.html')

def faculty_login_view(request):
    fac_login=Faculty_login_form()
    context={
        'fac_login':fac_login
    }
    if request.method=="POST":
        fac_login=Faculty_login_form(request.POST)
        fac_id=request.POST.get('fac_id')
        fac_password=request.POST.get('fac_password')
        if Faculty_profile_model.objects.filter(fac_id=fac_id).exists() and Faculty_profile_model.objects.filter(fac_password=fac_password).exists():  
            return redirect('faculty_profile',fac_id)

    return render(request,'faculty/faculty_login_display.html',context)

def faculty_profile_view(request,fac_id):
    obj_fac=Faculty_profile_model.objects.get(fac_id=fac_id)
    obj_std=Students_profile_model.objects.all()
    lecture_form=Faculty_profile_form(instance=obj_fac)
   # dox_form=Faculty_dox_form()
    context={
        'fac_profile_obj':obj_fac,
        'obj_std':obj_std,
        'lecture':lecture_form,
    #    'dox_form':dox_form
       
    }
    if request.method=="POST":
        print("post method in fac display")
     #   dox_form=Faculty_dox_form(request.POST)
        context={
        'fac_profile_obj':obj_fac,
        'obj_std':obj_std,
        'lecture':lecture_form,
  #      'dox_form':dox_form  
    }
        # if dox_form.is_valid():
        #     print('dox_valid')
        #     dox_form.save()

        #if lecture_form.is_valid():
            #print("valid lecture")
        return redirect('std_attend',fac_id)

        
    

    return render(request,'faculty/faculty_profile_display.html',context)

def faculty_std_academic_view(request,std_id):
    std_obj=Students_profile_model.objects.get(std_id=std_id)
    print(std_obj)
    std_form=Student_academics_form(request.POST or None,instance=std_obj)      
    context={
        'std_obj':std_obj,
        'std_form':std_form,
    }
    if request.method=="POST":
        if std_form.is_valid():
            std_form.save()
            
    return render(request, 'faculty/faculty_std_academic_display.html',context)

def faculty_student_attendance(request,fac_id):
    print("in the attend")
    def getkeys(dict): 
        list = [] 
        for key in dict.keys(): 
            list.append(key) 
        return list[1:] 
    def getvalues(dict): 
        list = [] 
        for key in dict.values(): 
            list.append(key) 
        return list[1:] 
    def to_int(l):
        list =[]
        for i in l:
            list.append(int(i))
        return list
    std_obj=Students_profile_model.objects.all()
    print(std_obj)
    form=Std_attendance_form()
    context={
        'std_object':std_obj
    }
    if request.method=="POST":
        form=Std_attendance_form(request.POST)
        fac_obj=Faculty_profile_model.objects.get(fac_id=fac_id)
        previous_total_lectures=fac_obj.total_lecures
        Faculty_profile_model.objects.filter(fac_id=fac_id).update(total_lecures=previous_total_lectures+1)
        # print(request.POST)
        l=getvalues(request.POST)
        l=to_int(l)
        # print(l)
        faculty_id=Faculty_profile_model.objects.get(fac_id=fac_id)#get the desired obj
        fac_course=(faculty_id.fac_course)#get the sub of that faculty
        # print(fac_course)
        # address=id(fac_course)
        #add=ctypes.cast(address, ctypes.py_object)

        for (i,j) in zip(range(1,9),l):
            stud_attend=Student_attendance_model.objects.get(id=i)
            std_sub=eval('stud_attend.' + fac_course)
            new_att=int(std_sub)+j
            # print(new_att)
            eval("Student_attendance_model.objects.filter(id="+str(i)+").update(" + fac_course +" = new_att)")

        return render(request,'faculty/demo.html')

            # print(stud_attend.ctypes.cast(address, ctypes.py_object).value)
    # print()
    context={
        'std_object':std_obj,
        'form':form
    }
   
    return render(request,'faculty/std_attendance_display.html',context)

    