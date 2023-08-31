from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('verify/', views.verify_certificate, name='verify_certificate'),
    path('contact/', views.contact_form_view, name='contact_form_view'),

  
  
]