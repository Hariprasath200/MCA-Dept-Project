from os import name
from django.shortcuts import render
from .models import*
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def child(request):
    image = Image.objects
    context={'image':image}
    return render(request,'prasath/home.html',context)
def event(request):
    return render(request,"prasath/event.html")
def staff(request):
    photos = Photo.objects.all()
    context= {'photos':photos}
    return render(request,"prasath/staff.html",context)
def about(request):
    return render(request,"prasath/about.html")
def contact(request):
    return render(request,"prasath/contact.html")
def Developer(request):
    return render(request,"prasath/Developer.html")
def registration_event(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))*100
        email= request.POST.get("email")
        client = razorpay.Client(auth=("rzp_test_Z1LjhqHWDoMeHH", "2aDqgtbGhBUPPKHocVZtEHOt")) 
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        registration_event = Registration(name=name,amount=amount,email = email,razorpay_payment_id=payment['id'])
        registration_event.save()
        return render(request,"prasath/registration_event.html",{'payment':payment})
    return render(request,"prasath/registration_event.html")
@csrf_exempt



def registration_payment(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razor_order_id":
                order_id = val
                break

        print(f"Received Razorpay Order ID: {order_id}")

        user = Registration.objects.filter(razorpay_payment_id=order_id).first()

        # Save the changes

        msg_plain = render_to_string('prasath/email.txt')
        msg_html = render_to_string('prasath/email.html')

        if user is not None:
            print(f"Found user with ID: {user.id}")
            print(f"Email Content: {msg_plain}")
            print(f"Recipient Email: {user.email}")

            send_mail("Your Registration successfully completed", msg_plain, settings.EMAIL_HOST_USER,
                      [user.email], html_message=msg_html)
    context={
        "user": name
        
    }
            
    return render(request, "prasath/registration_payment.html",context=context)
