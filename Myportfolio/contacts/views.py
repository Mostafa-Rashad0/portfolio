from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact(name=name, email=email, message=message).save()
        return redirect('thanks')
    return render(request,'contacts/contact.html')

def thanks(request):
    return render(request,'contacts/thanks.html')
