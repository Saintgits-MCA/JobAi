# Generated by Django 5.1.5 on 2025-02-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobAi_App', '0025_remove_company_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
    ]
