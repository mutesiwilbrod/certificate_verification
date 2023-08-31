from django.db import models

# Create your models here.
class Certificate(models.Model):
    certificate_number = models.CharField(max_length=100, unique=True)
    recipient_name = models.CharField(max_length=200)
    issue_date = models.DateField()

    COURSE_CHOICES = (
        ('Intern', 'Internship'),
        ('Short', 'Short course'),
        
        # Add more choices as needed
    )
    Course = models.CharField(max_length=200, choices=COURSE_CHOICES)
    
    def __str__(self):
        return f"{self.recipient_name} {self.recipient_name}"