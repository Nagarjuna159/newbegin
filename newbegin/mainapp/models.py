from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
Contacting_For_Choices = [
    ('Please Choose','Please Choose'),
    ('Training','Training'),
    ('Web Applications','Web Applications'),
    ('Android/IOS Apps','Android/IOS Apps')
]
 
Enquire_Course_Choices = [
    ("Python Web Development","Python Web Development"),
    ("Java Web Development","Java Web Development"),
    ("Full Stack Training","Full Stack Training"),
    ("Java & Python","Java & Python"),
]

def validate_phone(value):
    value=len(str(value))
    if value != 10:
        raise ValidationError(
    _('Phone number you entered is not valid. Phone number must contain 10 numbers'),
    params={'value':value}
    ) 
class Contact_Model(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField(validators=[validate_phone])
    contacting_for = models.CharField(max_length=30,choices=Contacting_For_Choices,default="Please Choose")
    message = models.TextField()

class Enquire_Course_Model(models.Model):
    name = models.CharField(max_length=60)
    select_course = models.CharField(max_length=30,choices=Enquire_Course_Choices,default="Python Web Development")
    email = models.EmailField()
    phone = models.IntegerField()
    