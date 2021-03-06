# Generated by Django 4.0.1 on 2022-01-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_student_department_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.AutoField(max_length=4, primary_key=True, serialize=False)),
                ('salary', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
