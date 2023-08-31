from django.contrib import admin
from .models import Certificate

# Register your models here.
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('recipient_name', 'certificate_number', 'issue_date', 'Course')

admin.site.register(Certificate, CertificateAdmin)
