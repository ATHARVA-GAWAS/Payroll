from email.policy import default

from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)



class Job(models.Model):
        name = models.CharField(max_length=200)
        job_ID = models.CharField(max_length=200)
        description = models.CharField(max_length=150)
        salary_range = models.CharField(max_length=200)
        dept_head = models.CharField(max_length=150)





class Project(models.Model):
    name = models.CharField(max_length=200)
    proj_id = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    project_status = models.CharField(max_length=200)


class Leave(models.Model):
    leave_id = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    start_date = models.DateField(max_length=200)
    end_date = models.DateField(max_length=200)
    reason = models.CharField(max_length=200)




class Salary(models.Model):
    salary_id = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    annual_package = models.CharField(max_length=200,null=True)
    payment_status = models.CharField(max_length=200)
    annual_increment = models.CharField(max_length=200)


    
class Login(models.Model):
    email_id= models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)

    def __str__(self):
        return self.emp_id

class ExcelFile(models.Model):
      file=models.FileField(upload_to="excel")

