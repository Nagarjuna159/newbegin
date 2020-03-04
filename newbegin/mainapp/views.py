from django.shortcuts import render,redirect
from .forms import Contact_form
from .models import Contact_Model
# Create your views here.
def index_view(request):
    return render(request,'mainapp/index.html')

def contact_view(request):
    context = {}
    form = Contact_form
    if request.method :
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact_form
    context['form'] = form
    return render(request,'mainapp/contact.html',context)