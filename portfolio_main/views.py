import datetime
import os
import boto
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from formal_portfolio.settings import RESUME_URL


def home(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')





def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def download_resume(request):
    new_pdf_file = 'Travis_Cockcroft_Resume.pdf'
    pdf = (os.path.join(RESUME_URL))
    with open(pdf, 'rb') as f:
        response = HttpResponse(f, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+new_pdf_file
        return response

