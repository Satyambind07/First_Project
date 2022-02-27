

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
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    intake = models.IntegerField(default=60)
    class Meta:
        db_table = "dept"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    marks = models.FloatField()
    is_active = models.BooleanField(default=1)
    active_objects = ActiveStudManager()
    inactive_objects = InActiveStudManager()
    objects = models.Manager()
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True)


class Subject(Common_Fields):
    is_practical = models.BooleanField(default=False)
    total_marks = models.IntegerField()
    Student = models.ManyToManyField(Student)

    class Meta:
        db_table = "subject"