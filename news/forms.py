from django import forms
from news.models import ContactUs,Subscriber

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name' , 'email_address', 'phone_number', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email',]
              