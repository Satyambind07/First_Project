# Generated by Django 4.0.1 on 2022-01-25 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_college_princi_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='princi',
            name='college',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.college'),
        ),
    ]