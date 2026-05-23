from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
      # ✅ حفظ رسالة التواصل
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, "تم إرسال رسالتك بنجاح 👍")

        return redirect('index') 
    context={
        'products': Product.objects.all(),
        "offer": Offer.objects.first(),
    }
    
    return render(request,"index.html",context)



 