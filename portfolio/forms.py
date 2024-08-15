from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ["name","email","message",]
    
    def clean(self):
 
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
         
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        
        content = self.cleaned_data.get('message')
        # (print(name))
        # conditions to be met for the username length
        if name:
            if len(name) < 3:
                raise forms.ValidationError("Must be at least 3 characters")
            #     self._errors['name'] = self.error_class([
            #         'Minimum 3 characters required'])
        else:
            self._errors['name'] = self.error_class([
                    'name is required'])
        if not content:
            self._errors['message'] = self.error_class([
                    'message is required'])
        return self.cleaned_data
    