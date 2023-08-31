from django.shortcuts import render
from .models import Certificate
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

import os
# Create your views here.
def index (request):
    return render(request, 'certificate_verification/index.html', {})

# def certificate_view(request, certificate_number):
#     certificate = get_object_or_404(Certificate, certificate_number=certificate_number)
#     context = {'certificate': certificate}
#     return render(request, 'certificate_verification/index.html', context)
# def verify_certificate(request):
#   if request.method == 'POST':
#     certificate_number = request.POST.get('certificate_number')
    
#     try: 
#       certificate = Certificate.objects.get(certificate_number=certificate_number)
      

#       return render(request, 'certificate_verification/verification_result.html', {'certificate': certificate})
      
#     except Certificate.DoesNotExist:
#       return JsonResponse({'status': 'error'})

#   return render(request, 'certificate_verification/verification_result.html')
def verify_certificate(request):
    if request.method == 'POST':
        certificate_number = request.POST.get('certificate_number')
        try:
            certificate = Certificate.objects.get(certificate_number=certificate_number)
            certificate_data = {
                "recipient_name": certificate.recipient_name,
                "issue_date": certificate.issue_date.strftime('%Y-%m-%d'),
                "Course": certificate.get_Course_display()  # Use get_FOO_display() for choices
            }
            
            print(certificate_data)

            return JsonResponse({'status': 'success', 'certificate_data': certificate_data})
        except Certificate.DoesNotExist:
            return JsonResponse({'status': 'error'})
    
    return render(request, 'certificate_verification/index.html')  # Replace 'your_template.html' with your actual template path
# Inside your view function
# def verify_certificate(request):
#     if request.method == 'POST':
#         certificate_number = request.POST.get('certificate_number')
#         try:
#             certificate = Certificate.objects.get(certificate_number=certificate_number)
#             certificate_data = {
#                 'recipient_name': certificate.recipient_name,
#                 'issue_date': certificate.issue_date.strftime('%Y-%m-%d'),
#             }
#             return render(request, 'certificate_verification/verification_result.html', {'status': 'success', 'certificate_data': certificate_data})
#         except Certificate.DoesNotExist:
#             return render(request, 'certificate_verification/verification_result.html', {'status': 'error'})
    
#     return render(request, 'certificate_verification/verification_result.html')

def contact_form_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('Name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        issue = request.POST.get('issue')
        subject = 'Contact Form Submission'
        message = f'Full Name: {full_name}\nPhone Number: {phone_number}\nEmail: {email}\nIssue: {issue}'
        from_email = 'verifyprimacy@gmail.com'
        recipient_list = ['verifyprimacy@gmail.com']
        print(recipient_list)
        #send_mail(subject, message, from_email, recipient_list)
    
        try:
            send_mail(subject, message, from_email, recipient_list)
            print("LLLLLLLLLLLLLLLLL", send_mail)
            return render(request, 'certificate_verification/success.html')
        except Exception as e:
            print("Error sending email>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:", e)
            return render(request, 'certificate_verification/index.html')

    return render(request, 'certificate_verification/index.html')





# def generate_certificate_number():
#     # ... same as before ...
#     return render(request, 'certificate_verification/generated.html', {'certificates': certificates})
# def generate_certificates(request):
#     certificates = Certificate.objects.all()
#     output_folder = 'new_certificates'
#     os.makedirs(output_folder, exist_ok=True)
        
#     for cert in certificates:
#             # ... same as before ...

#         return render(request, 'certificate_verification/generated.html', {'certificates': certificates})