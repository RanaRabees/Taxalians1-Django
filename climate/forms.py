
from cProfile import label
from tkinter import Image
from django import forms
from .models import image

class ImageForm (forms.ModelForm):
    class Meta : 
        model = Image
        fields = '__all__'
        labels = {'photo':''} 