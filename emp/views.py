from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import pandas as pd
from django.conf import settings
import uuid

from .serializers import *


def emp_home(request):
    return render(request,"emp/home.html",{})

def emp_view_employee(request):
    emps=Emp.objects.all()
    return render(request,"emp/view_employee.html",{'emps':emps})

def emp_login(request):
    emps=Emp.objects.all()
    return render(request,"emp/login.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/view_employee/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/view_employee/")


def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/view_employee/")
def job_dept(request):
    job=Job.objects.all()
    return render(request,"emp/job_dept.html",{'emps':job})
def add_job(request):
    if request.method=="POST":
        name = request.POST.get("name")
        job_ID = request.POST.get("job_ID")
        description = request.POST.get("description")
        salary_range = request.POST.get("salary_range")
        dept_head = request.POST.get("dept_head")
        e = Job(name = name,job_ID = job_ID,description = description,salary_range = salary_range, dept_head = dept_head)
        e.save()
        return redirect("/emp/job-dept/")
    return render(request,"emp/add_job.html",{})

def delete_job(request,job_ID):
    emp=Job.objects.get(pk=job_ID)
    emp.delete()
    return redirect("/emp/job-dept/")

def update_job(request,job_ID):
    job=Job.objects.get(pk=job_ID)
    print("Yes Bhai")
    return render(request,"emp/update_job.html",{
        'emps':job
    })
def do_update_job(request,job_ID):
    if request.method=="POST":
        job_name=request.POST.get("job_name")
        job_ID=request.POST.get("job_ID")
        description=request.POST.get("description")
        salary_range=request.POST.get("salary_range")
        dept_head=request.POST.get("dept_head")
        e=Job.objects.get(pk=job_ID)
        e = Emp.objects.get(pk=job_ID)
        e.job_ID=job_ID
        e.name=job_name
        e.description=description
        e.salary_range=salary_range
        e.dept_head=dept_head
        e.save()
    return redirect("/emp/job_dept/")
def project(request):
    emps=Project.objects.all()
    return render(request,"emp/Project.html",{'emps':emps})
def add_project(request):
    if request.method=="POST":
        name = request.POST.get("name")
        proj_id = request.POST.get("proj_id")
        description = request.POST.get("description")
        project_status = request.POST.get("project_status")
        e = Project(name = name,proj_id = proj_id,description = description, project_status= project_status)
        e.save()
        return redirect("/emp/Project/")
    return render(request,"emp/add_project.html",{})
def leaves(request):
    emps=Leave.objects.all()
    return render(request,"emp/leave.html",{'emps':emps})
def add_leave(request):
    if request.method=="POST":
        leave_id = request.POST.get("leave_id")
        emp_id = request.POST.get("emp_id")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        reason=request.POST.get("reason")
        e = Leave(leave_id = leave_id,emp_id = emp_id,start_date = start_date,end_date=end_date, reason= reason)
        e.save()
        return redirect("/emp/leave/")
    return render(request,"emp/add_leave.html",{})
def salaries(request):
    emps=Salary.objects.all()
    return render(request,"emp/salary.html",{'emps':emps})
def add_salaries(request):
    if request.method=="POST":
        salary_id = request.POST.get("salary_id")
        emp_id = request.POST.get("emp_id")
        annual_package = request.POST.get("annual_package")
        payment_status = request.POST.get("payment_status")
        annual_increment=request.POST.get("annual_increment")
        e = Salary( salary_id =  salary_id,emp_id = emp_id,annual_package = annual_package, payment_status = payment_status ,annual_increment= annual_increment)
        e.save()
        return redirect("/emp/salary/")
    return render(request,"emp/add_salary.html",{})

def login(request):
    if request.method=="POST":
        email_id=request.POST.get("email_id")
        password=request.POST.get("password")
        emp_id = request.POST.get("emp_id")

        if email_id in Login.email_id():
            if  email_id.password == password:
               return redirect("/emp/home/")
            else:
                  return redirect("/emp/home/")
        else:
             return redirect("/emp/login/")
    return render(request,"emp/login.html",{})

from django.http import HttpResponse
from django.template import loader


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )
    

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
        ({{Emp.name}},{{Emp.emp_id}},{{Emp.phone}},{{Emp.department}},{{Emp.address}})
    )

    t = loader.get_template("emp/my_template_name.txt")
    c = {"data": csv_data}
    response.write(t.render(c))
    return response






def export_data_to_excel(request):
    objs=Job.objects.all()
    serializer=JobSerializer(objs,many=True)
    data=pd.DataFrame(serializer.data)
    print(data)


    data.to_excel('output.xlsx')
    return JsonResponse({ 'status':200})

def import_data_to_db(request):
    if request.method=='POST':
        file=request.FILES['files']
        obj=ExcelFile.objects.create(file=file)
        path = str(obj.file)
        print(f'{settings.BASE_DIR}/{path}')
        df=pd.read_excel(path)
        for d in df.values:
              print(df)


    return render(request,'emp/excel.html')
def export_salary_data_to_excel(request):
    objs=Salary.objects.all()
    serializer=SalarySerializer(objs,many=True)
    data=pd.DataFrame(serializer.data)
    print(data)


    data.to_excel('salary_output.xlsx')
    return JsonResponse({ 'status':200})
def export_project_data_to_excel(request):
    objs=Project.objects.all()
    serializer=ProjectSerializer(objs,many=True)
    data=pd.DataFrame(serializer.data)
    print(data)


    data.to_excel('project_output.xlsx')
    return JsonResponse({ 'status':200})
def export_leave_data_to_excel(request):
    objs=Leave.objects.all()
    serializer=LeaveSerializer(objs,many=True)
    data=pd.DataFrame(serializer.data)
    print(data)


    data.to_excel('leave_output.xlsx')
    return JsonResponse({ 'status':200})
def export_emp_data_to_excel(request):
    objs=Emp.objects.all()
    serializer=EmpSerializer(objs,many=True)
    data=pd.DataFrame(serializer.data)
    print(data)


    data.to_excel('emp_output.xlsx')
    return JsonResponse({ 'status':200})