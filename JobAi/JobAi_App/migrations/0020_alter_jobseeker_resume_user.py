# Generated by Django 5.1.5 on 2025-02-17 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobAi_App', '0019_jobseeker_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker_resume',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JobAi_App.jobseeker_registration'),
        ),
    ]
