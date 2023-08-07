from django.shortcuts import render,redirect
from MainApp.models import Contact, NewsLetter

from django.contrib import messages


# Create your views here.




def HomePage(request):
    if request.method == 'POST':
        email = request.POST['email']

        # Create a new NewsLetter instance and assign the form data
        newsletter = NewsLetter(email=email)
        
        # Save the new NewsLetter instance to the database
        newsletter.save()
        
        
        messages.success(request, 'Email Received, Thanks for subscribing')

        # Add any additional logic or actions as needed

    context = {}
    return render(request, "pages/index.html", context)



def Services(request):
    context = {}
    return render(request, "pages/service.html",context)


def ContactUS(request):
    
    if request.method == 'POST':
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Create a new Contact instance and assign the form data
        contact = Contact(fullname=fullname, email=email, subject=subject, message=message)
        
        # Save the new Contact instance to the database
        contact.save()

        # Display a success message
        messages.success(request, 'Message sent! We will get back to you soon.')

        # Redirect back to the contact form
        return redirect('contact')
    else:
        # Render the contact form template for GET requests
        return render(request, 'pages/contact.html')
def Projects(request):
    context = {}
    return render(request, "pages/project.html",context)

