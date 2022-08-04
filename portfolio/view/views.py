from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'home': True})


def contact(request):
    return render(request, 'contact/contact_form.html')