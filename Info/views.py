from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('xabarlar')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def messages_view(request):
    contacts = Contact.objects.all()

    return render(request, 'messages.html', {'contacts': contacts})