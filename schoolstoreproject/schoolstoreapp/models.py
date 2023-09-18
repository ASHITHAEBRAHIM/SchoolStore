from django.db import models
# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class purpose(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class std_form(models.Model):
    std_name = models.CharField(max_length=250)
    DOB = models.DateField('DOB')
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=250,blank=True)
    address = models.CharField(max_length=250,blank=True)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    course = models.ForeignKey(course,on_delete=models.CASCADE)
    purpose = models.ForeignKey(purpose,on_delete=models.SET_NULL,blank=True,null=True)
    materials_provided = models.CharField(max_length=250)
    def __str__(self):
        return self.std_name

