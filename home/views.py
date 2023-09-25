from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def home(request):
    print("Request Method: ", request.method)
    print("Query Parameters: ", request.GET)
    # print("RESPONSE:    ",response)
    return render(request, "index.html", context={"params": request.GET.dict()})


def about(request):
    return render(request, "about.html")


from home.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, "contact.html", {"form": form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                from_email=settings.EMAIL_HOST_USER,
                subject="Blog Contact Message",
                recipient_list=[form.cleaned_data.get("email")],
                message=form.cleaned_data.get("message"),
            )
            return redirect(reverse("contact"))
        return render(request, "contact.html", {"form": form})


def handle_404(request):
    return render(request, "errors/404.html")


def handle_unauthorized(request):
    return render(request, "errors/not_authorized.html")
