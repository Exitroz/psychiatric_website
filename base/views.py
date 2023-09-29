from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def doctors(request):
    return render(request, "doctors.html")

def services(request):
    return render(request, "services.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def appointment(request):
    return render(request, "appointment.html")

def faq(request):
    return render(request, "faq.html")

