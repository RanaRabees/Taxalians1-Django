
from tkinter import Image
from django.http import HttpResponse
from django.shortcuts import render
from climate.models import School
from . import views
from  django import forms
# from climate.models import image

def home(request):
    return render(request,'home.html')

def spring(request):
    return render(request,'spring.html')

def imageuploader(request):
    return render(request,'imageuploader.html')

# def home(request):
#     if request.method == "POST":
#        form = image(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#            form = image()
#            img = Image.objects.all    
#     return render(request,'home.html')

# def home(request):
#     a=''
#     ranag=request.POST.get('text','default')
#     remove_punc=request.POST.get('remove_punc','off')
#     if remove_punc == "on" :
#         punctuations = '''?`,:,@;,%^<{<,,,>>>..!!]}!|“”,_-(),,[],,*,\\\::"""'~,/,,#,$,&''' 
#         analyzed=""
#         for i in ranag:
#             if i not in punctuations:
#                analyzed=analyzed+i 
#         data={'remove_punc':remove_punc,'btext':analyzed}         
#         return render(request,'home.html',data)
#         a='your message has been sent'   
#     else:
#         return HttpResponse("Ha Ha Ha app ne sub kuch khatam kar diya he")



def summer(request):
    return render(request,'summer.html')



def winter(request):  
    return render(request,'winter.html')       


def autumn(request):
    return render(request,'autumn.html')


def base(request):  
    return render(request,'base.html') 



def index(request):  
    return render(request,'index.html') 



# def spring(request):    
#     b=''
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         father_name=request.POST.get('father_name')
#         gender=request.POST.get('gender')
#         Class=request.POST.get('Class')
#         section=request.POST.get('section')
#         roll_no=request.POST.get('roll_no')                 
#         data=School(name=name,father_name=father_name,gender=gender,Class=Class,section=section,roll_no=roll_no)
#         data.save()
#         b='your data has been sent sir you can go and check'
#     return render(request,'base.html',{'b':b})
    
   
