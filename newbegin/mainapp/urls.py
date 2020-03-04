from django.urls import path
from mainapp import views
urlpatterns=[
    path('',views.index_view,name='index'),
    path('contact',views.contact_view,name='contact')
]