from django.db import models

# Create your models here.
class Students_profile_model(models.Model):
    std_id = models.DecimalField(max_digits=10,decimal_places=0,unique=True)
    std_name = models.CharField(max_length=30)
    std_password=models.CharField(max_length=10,blank=True)
    std_year=models.CharField(max_length=20)
    std_branch=models.CharField( max_length=50)
    std_dob=models.DateField(null=True)
    std_phone_no=models.DecimalField(decimal_places=0, max_digits=10)
    std_parent_phone_no=models.DecimalField(decimal_places=0, max_digits=10)
    std_fathers_name=models.CharField( max_length=50)
    std_mothers_name=models.CharField( max_length=50)
    std_email=models.EmailField( max_length=250)
    std_parent_email=models.EmailField( max_length=250)

    s1_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s1_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s1_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    
    s2_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s2_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s2_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    s3_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s3_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s3_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    s4_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s4_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s4_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    s5_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s5_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s5_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    s6_tt1=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s6_tt2=models.DecimalField(max_digits=2,decimal_places=0,default=0)
    s6_sem1=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    def __str__(self):
        return self.std_name

class Student_attendance_model(models.Model):
    std_id = models.DecimalField(max_digits=10,decimal_places=0,unique=True)
    subject1=models.DecimalField(decimal_places=0, max_digits=2)
    subject2=models.DecimalField(decimal_places=0, max_digits=2)
    subject3=models.DecimalField(decimal_places=0, max_digits=2)
    subject4=models.DecimalField(decimal_places=0, max_digits=2)
    subject5=models.DecimalField(decimal_places=0, max_digits=2)
    subject6=models.DecimalField(decimal_places=0, max_digits=2)
    
