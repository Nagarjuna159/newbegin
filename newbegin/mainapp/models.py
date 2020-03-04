from django.db import models

# Create your models here.
Contacting_For_Choices = [
    ('Please Choose','Please Choose'),
    ('Training','Training'),
    ('Web Applications','Web Applications'),
    ('Android/IOS Apps','Android/IOS Apps')
]

class Contact_Model(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    contacting_for = models.CharField(max_length=30,choices=Contacting_For_Choices,default="Please Choose")
    message = models.TextField()