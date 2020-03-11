from django.shortcuts import render,redirect
from .forms import Contact_form, Enquire_Course_Form
from .models import Contact_Model, Enquire_Course_Model
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

def about_view(request):
    return render(request,'mainapp/about.html')

def pyweb_view(request):
    return render(request,'mainapp/pyweb.html')

def javapy_view(request):
    return render(request,'mainapp/java_py_combo.html')

def fullstack_view(request):
    return render(request,'mainapp/fulls.html')

def java_view(request):
    return render(request,'mainapp/java.html')

def enquire_course_view(request):
    context = {}
    form = Enquire_Course_Form
    if request.method :
        form = Enquire_Course_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thankyou')
            
    else:
        form = Enquire_Course_Form
    context['form'] = form
    return render(request,'mainapp/Enquire.html',context)

def thankyou_view(request):
    return render(request,'mainapp/thankyou.html')