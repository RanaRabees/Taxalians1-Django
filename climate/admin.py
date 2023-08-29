from tkinter import Image
from django.contrib import admin
from .models import vidimage
# Register your models here.
from .models import School
admin.site.register(School)

from .models import Image
admin.site.register(Image)


@admin.register(vidimage)
class imageadmin(admin.ModelAdmin):
    list_display = ['id','photo','date']