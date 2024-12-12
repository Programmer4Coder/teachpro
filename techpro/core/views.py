from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Slider, About, Service, Why_choose_us, Blog, Contact

def home(request):
    # Fetch data for the home page
    slider = Slider.objects.first()
    about = About.objects.first()  # Fetch the first About object
    service = Service.objects.all()
    wcu = Why_choose_us.objects.first()
    blog = Blog.objects.all()
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject") 
        phone = request.POST.get("phone")
        question = request.POST.get("question")

        # Compose the message
        message = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}
        Phone: {phone}
        Question: {question}
        """

        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email="bishtakash668@gmail.com",  # Use your verified sender email
            recipient_list=["akashbisht457@gmail.com"],  # Recipient's email
            fail_silently=False,  # Raise errors for debugging if email fails
        )
    
    return render(
        request,
        'home.html',
        {
            'slider': slider,
            'about': about,
            'service': service,
            'wcu': wcu,
            'blog': blog,
            'contact': contact
        },
    )

# from django.shortcuts import render
# from .models import Slider,About,Service,Why_choose_us,Blog,Contact
# from .forms import ContactForm

# def home(request):
#     slider = Slider.objects.first()
#     about = About.objects.first()  # Fetch the first About object
#     service = Service.objects.all()
#     wcu = Why_choose_us.objects.first()
#     blog = Blog.objects.all()
#     contact = Contact.objects.first()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form (e.g., save to the database or send an email)
#             # Example: form.save() or send an email
#             return render(request, 'home.html')  # Redirect to a success page
#     else:
#         form = ContactForm()

#     return render(request, 'home.html', {'slider': slider, 'about': about, 'service': service, 'wcu': wcu, 'blog': blog, 'contact':contact, 'form': form})
