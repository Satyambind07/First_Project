from django.contrib import admin
from .models import Department, Student, College, Princi, Subject

# Register your models here.

admin.site.register([Student, College, Princi, Department, Subject])