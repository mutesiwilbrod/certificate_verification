# Generated by Django 4.2.4 on 2023-08-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_verification', '0002_rename_issuer_name_certificate_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='Course',
            field=models.CharField(choices=[('math', 'Mathematics'), ('science', 'Science'), ('history', 'History'), ('english', 'English')], max_length=200),
        ),
    ]
