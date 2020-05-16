from django import forms
from .models import *
from datetimepicker.widgets import DateTimePicker
from datetimepicker.helpers import js_loader_url




class client_form(forms.ModelForm):
    


    first_name=forms.CharField(widget=forms.TextInput(),required=True)
    middle_name=forms.CharField(widget=forms.TextInput(),required=True)
    last_name=forms.CharField(widget=forms.TextInput(),required=True)
    gmail=forms.EmailField(widget=forms.TextInput(),required=True)
    code=forms.CharField(widget=forms.TextInput(),required=True)
    phone=forms.CharField(widget=forms.TextInput(),required=True)
    occupation=forms.CharField(widget=forms.TextInput(),required=False)
    status=forms.CharField(widget=forms.TextInput(),required=False)
    people_mens=forms.CharField(widget=forms.TextInput(),required=False)
    people_female=forms.CharField(widget=forms.TextInput(),required=False)
    people_childern=forms.CharField(widget=forms.TextInput(),required=False)
    any_message=forms.CharField(widget=forms.TextInput(),required=False)
    address_line1=forms.CharField(widget=forms.TextInput(),required=True)
    address_line2=forms.CharField(widget=forms.TextInput(),required=True)
    zip1=forms.CharField(widget=forms.TextInput(),required=True)
    city=forms.CharField(widget=forms.TextInput(),required=True)
    state=forms.CharField(widget=forms.TextInput(),required=True)
    country=forms.CharField(widget=forms.TextInput(),required=True)
    Date_From = forms.CharField(widget=forms.TextInput(),required=True)
    Date_To =forms.CharField(widget=forms.TextInput(),required=True)
    mode=forms.CharField(widget=forms.TextInput(),required=True)
   
    city_name= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), required=False)
   
    

    
    class Meta():
        model = clientdetails 
        fields = ['first_name','middle_name','last_name','gmail','code','phone','occupation','status','people_mens','people_female','people_childern','any_message','address_line1','address_line2','zip1','city','state','country','Date_From','Date_To','mode','city_name']
   


