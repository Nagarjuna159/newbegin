from django.contrib import admin
from .models import Contact_Model
# Register your models here.
class Contact_admin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','contacting_for']

admin.site.register(Contact_Model,Contact_admin)