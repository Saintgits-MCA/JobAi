# Generated by Django 5.1.5 on 2025-02-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobAi_App', '0011_company_jobs_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_jobs',
            name='job_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company_jobs',
            name='job_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
