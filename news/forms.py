from django import forms
from news.models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name' , 'email_address', 'phone_number', 'message']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')

    #     if not first_name or not last_name:
    #         raise forms.ValidationError("Both first name and last name are required.")
        
    #     return cleaned_data
    

              