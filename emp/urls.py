from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('export_data_to_excel/',export_data_to_excel),
    path('import_data_to_db/',import_data_to_db),
    path("login/",login),
    path("home/",emp_home),
    path("view_employee/",emp_view_employee),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path("job-dept/",job_dept),
    path("add-job/",add_job),
    path("update-job/<int:job_ID>",update_job),
    path("delete-job/<int:job_ID>",delete_job),
    path("do-update-job/<int:job_ID>",do_update_job),
    path("Project/",project),
    path("add-project/",add_project),
    path("leave/", leaves),
    path("add-leave/", add_leave),
    path("salary/", salaries),
    path("add-salary/", add_salaries),
    path("delete-job/<int:emp_id>",delete_job),
]
