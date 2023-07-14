from django.urls import path
from . import views

urlpatterns = [
 path('convert/', views.html_to_pdf, name='html_to_pdf'),
 ]
