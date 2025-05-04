from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    form = ContactForm()  # Initialize the form for GET requests
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            service = form.cleaned_data['service']
            message = form.cleaned_data['message']

            # Print the form data (consider using logging instead of print)
            print(f"Name: {name}, Email: {email}, Phone: {phone}, Service: {service}, Message: {message}")
            form.save()


            try:
                # Send the email
                send_mail(
                    f'New message from {name}',
                    f'Name: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nMessage: {message}',
                    settings.DEFAULT_FROM_EMAIL,  # Use a valid sender email
                    ['mindtrixindia@gmail.com'],  # Ensure this is set correctly
                    fail_silently=True,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')  # Redirect to a success page
            except Exception as e:
                # Log the exception for debugging
                print(f"Error sending email: {e}")
                messages.error(request, 'There was an error sending the email. Please try again later.')
                return redirect('contact')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about-2.html')

def services(request):
    return render(request, 'service-3.html')

def project(request):
    return render(request, 'project.html')

def team(request):
    return render(request, 'team.html')

def career(request):
    return render(request, 'career.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    form = ContactForm()  # Initialize the form for GET requests
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            service = form.cleaned_data['service']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Print the form data (consider using logging instead of print)
            print(f"Name: {name}, Email: {email}, Phone: {phone}, Service: {service}, Message: {message}")
            form.save()

            try:
                # Send the email
                send_mail(
                    f'New message from {name}',
                    f'Name: {name}\nEmail: {email}\nPhone: {phone}\nServices: {service}\nMessage: {message}',
                    settings.DEFAULT_FROM_EMAIL,  # Use a valid sender email
                    ['mindtrixindia@gmail.com'],  # Ensure this is set correctly
                    fail_silently=True,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('success_page')  # Redirect to a success page
            except Exception as e:
                # Log the exception for debugging
                print(f"Error sending email: {e}")
                messages.error(request, 'There was an error sending the email. Please try again later.')
                return redirect('contact')

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)




    # form = ContactForm()
    #
    # if request.method == "POST":
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    #     else:
    #         form = ContactForm()
    #
    # return render(request, 'contact.html', {'form': form})
    # form = ContactForm()  # Initialize the form for GET requests
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         service = form.cleaned_data['service']
    #         message = form.cleaned_data['message']
    #
    #         # Log the form data
    #         logger.info(f"Name: {name}, Email: {email}, Service: {service}, Message: {message}")
    #         print(f"Name: {name}, Email: {email}, Service: {service}, Message: {message}")
    #
    #         # Send the email without try-except
    #         send_mail(
    #             f'New message from {name}',
    #             f'Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message}',
    #             settings.DEFAULT_FROM_EMAIL,
    #             [settings.RECIPIENT_EMAIL],
    #             fail_silently=True,
    #         )
    #         messages.success(request, 'Your message has been sent successfully!')
    #         return redirect('contact')  # Redirect to a success page
    #
    # context = {
    #     'form': form,
    # }
    #
    # return render(request, 'contact.html', context)
