from django.db import models

# Create your models here.




#model for profile of faculty
class Faculty_profile_model(models.Model):
    fac_id=models.DecimalField(max_digits=10,decimal_places=0,unique=True)
    fac_name=models.CharField(max_length=100)
    fac_password=models.CharField(max_length=10,blank=True)
    fac_course=models.CharField(max_length=60)
    fac_qaulification=models.CharField(max_length=60)
    fac_department=models.CharField(max_length=60)
    fac_designation=models.CharField(max_length=60)
    fac_email=models.EmailField(max_length=200)
    fac_date_of_joining=models.DateField()
    # fac_file_name1=models.CharField(max_length=60,blank=True)
    # fac_file1=models.FileField(blank=True)
    # fac_file_name2=models.CharField(max_length=60,blank=True)
    # fac_file2=models.FileField(blank=True)
    
    total_lecures=models.DecimalField(max_digits=2,decimal_places=0,default=0)

    def __str__(self):
        return self.fac_name

