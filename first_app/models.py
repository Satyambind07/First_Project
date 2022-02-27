from xml.dom import ValidationErr
from django.db import models
from statistics import mode

# Create your models here.
# >>> exec(open("D:\\b6\\Django\\first_project\\first_app\\db_shell.py").read())

class ActiveStudManager(models.Manager):
    def get_queryset(self):
        return super(ActiveStudManager, self).get_queryset().filter(is_active=1)

class InActiveStudManager(models.Manager):
    def get_queryset(self):
        return super(InActiveStudManager, self).get_queryset().filter(is_active=0)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    marks = models.FloatField()
    is_active = models.BooleanField(default=1)
    active_objects = ActiveStudManager()
    inactive_objects = InActiveStudManager()
    objects = models.Manager()
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_active_student(cls):
        all_active_data = cls.objects.filter(is_active=1)
        return all_active_data

    def get_stud_details(self):
        print(f"""
        Student ID- {self.id}
        Student Name- {self.name}
        Student Age- {self.age}
        Student Marks- {self.marks}""")

    @classmethod
    def get_avg_marks(cls):
        all_data = cls.objects.all()
        total = 0
        for i in all_data:
            total += i.marks
        length = len(all_data)
        avg = total/len(all_data)
        return avg



class Common_Fields(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class College(Common_Fields):
    address = models.CharField(max_length=200)
    
    class Meta:
        db_table = "college"
        
class Princi(Common_Fields):
    college = models.OneToOneField(College , on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "princi"


class Department(Common_Fields):
    name = models.CharField(max_length=100, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name="depts")
    intake = models.IntegerField(default=60)
     
    class Meta:
        db_table = "dept"

# class Students(Common_Fields):
#     marks = models.FloatField()
#     is_active = models.BooleanField(default=True)
#     Department = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
#     class Meta:
#         db_table = "student"

class Subject(Common_Fields):
    is_practical = models.BooleanField(default=False)
    total_marks = models.IntegerField()
    Student = models.ManyToManyField(Student)

    class Meta:
        db_table = "subject"


class Employee(Common_Fields):
    emp_id = models.CharField(primary_key=True, max_length=4)
    salary = models.IntegerField(null=True)

    class Meta:
        db_table = "employee"

    def save(self, *args, **kwargs):
        if not self.emp_id:
            raise ValidationErr("emp_id should be passed")
        super(Employee, self).save(*args, **kwargs)