#  exec(open("D:\\b6\\Django\\first_project\\first_app\\db_shell.py").read())

from os import name
from first_app.models import *
from django.contrib.auth.models import User

# stud_data = Student.objects.all()
# print(stud_data)
# first_stud = Student.objects.first()
# print(first_stud.anme)

# data = Student.objects.filter(id__gte=3)
# print(data)

# try:
#     single_data = Student.objects.get(id=4)
#     # single_data.get_stud_details()
#     # print(single_data)
#     # single_data.delete()
# except Student.DoesNotExist:
#     print("No Data found")

# def increment_marks():
    # all_data = Student.objects.all()
    # all_data.delete()

    # for stud in all_data:
    #     stud.marks += (stud.marks*(5/100))
    #     stud.save()

# increment_marks()

# Student.

# object create--
# stud1 = Student(name="www", age=18, marks=45)
# stud1.save()
    
# stud2 = Student.objects.create(name="iii", age=23, marks=44)
# print(stud2)

# print(Student.objects.count())
# print(Student.get_active_student())

# object--- model manager--default

# Student.passed_obj.all()

# print(Student.active_objects.all())
# print(Student.inactive_objects.all())

# print(Student.objects.all())

# all_data = Student.objects.all().values("id" , "name")
# for i in all_data:
    # print(i)


# all_users = User.objects.all()
# print(all_users[1])

# all_data = Student.objects.all()
# print(all_data)


# e = Employee(emp_id="1521", salary=70000)
# e.save()


# data = Student.objects.all().order_by("-name")
# print(data)

try:
    c1 = College.objects.get(name="PRMCEAM")
except College.DoesNotExist:
    print("College does not exist....")
else:
    print(c1)

# print(c1.princi)

# print(c1.department_set.all())

# d1 = Department.objects.get(name="Electrical")
# print(d1.student_set.all())

# s1 = Student.objects.get(name="aaa", age=24)
# print(s1)
# print(s1.subject_set.all())

# problem while running-------------
dept = c1.department_set.all().filter(name="Electrical")[0]
ele_students = dept.student_set.all()
print(ele_students)


# student_list = []
# depts = c1.depts.all()
# print(depts)

# for dept in depts:
#     studs = dept.student_set.all()
#     student_list.extend(studs)

# print(student_list)

# subjects_list = set()
# for stud in student_list:
#     subs = stud.subject_set.all()
#     subjects_list.update(subs)

# print({stud.subject_set.all()})
# print(subjects_list)

# s1 = Student.objects.get(id=2)
# print(s1.department.college.princi)

# s = Student.objects.all()
# for i in s:
#     print(i.department)

# s1 = Subject.objects.first()
# print(s1.Student.filter(name_istartswith="A"))    #i diya hai wo case insensitive ke liy

# subs = Subject.objects.filter(Student__name = "aaa")
# print(subs)

# subs = Subject.objects.filter(Student__department__name="Electrical")
# print(subs)

# subs = Subject.objects.filter(Student__department__college__name="PRMCEAM").values("name", "total_marks")
# print(subs)

# c1 = College.objects.create(name="Raisoni College", address ="Bari")

# c1 = College.objects.filter(name="Raisoni College")
# print(c1)

# p = Princi.college.objects.create(name="Desh", college_id=3)

# d1 = Department.objects.create(name="IT", intake=90, college_id=3)
# print(d1.id)

# subs = Subject.objects.filter(Student__name="aaa")
# print(subs)
# stud1 = Student.objects.get(name="bbb")
# Subject.objects.create(name="Python", is_practical=True, total_marks=150)
# s1 = Subject.objects.get(name="Python")
# print(s1)
# s1.Student.add(stud1)
# # s1.Student