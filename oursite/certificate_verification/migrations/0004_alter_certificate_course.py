# Generated by Django 4.2.4 on 2023-08-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_verification', '0003_alter_certificate_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='Course',
            field=models.CharField(choices=[('Intern', 'Internship'), ('Short', 'Short course')], max_length=200),
        ),
    ]
