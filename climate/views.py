# from django.core.mail import send_mail
# from django.urls import is_valid_path
# from .forms import ImageForm
# from .models import image


from django.http import HttpResponse
from django.shortcuts import render


def climate(request):        
    return render(request,'climate.html')







# def climate(request):    
#     if request.method == "POST":
#        form = image(request.POST , request.FILES) 
#        if form.is_valid():      
#         form.save()       
#         form = ImageForm()
#         img = image.objects.all()       
#         return render(request,'climate.html',{'img':img,'form':form})
                             