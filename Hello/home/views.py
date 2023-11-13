from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Port
from .resouces import PortResource
from tablib import Dataset


def simple_upload(request):
    if request.method == 'POST':
        try:
            port_resource = PortResource()
            dataset = Dataset()
            new_port = request.FILES['myfile']

            if not new_port.name.endswith('xlsx'):
                messages.info(request, 'Wrong format. Please upload an Excel file.')
                return render(request, 'upload.html')

            imported_data = dataset.load(new_port.read(), format='xlsx')

            for data in imported_data:
                value = Port(
                    ip=data[0],
                    port=data[1],
                    powerLevel=data[2]
                )
                value.save()

            messages.success(request, 'File uploaded successfully.')

        except Exception as e:
            messages.error(request, f'Error during file upload: {e}')

    return render(request, 'upload.html')


def home(request):
    messages.success(request,"this is a test msg")
    return render(request,'index.html')


def router(request):
    return render(request,'routers.html')


def service(request):
    return render(request,'service.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Message has been sent")

    return render(request,'contact.html')
