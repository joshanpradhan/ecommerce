from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'billing_profile',
            # 'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'mobile_number',
            'postal_code',
        ]
        # widgets={
        #            "billing_profile":forms.TextInput(attrs={'class':'form-control'}),
        #            "address_type":forms.TextInput(attrs={'class':'form-control'}),
        #            "address_line_1":forms.TextInput(attrs={'placeholder':'Eg: New Baneshwor','class':'form-control'}),
        #            "address_line_2":forms.TextInput(attrs={'placeholder':'Eg: Shanitnagar Gate','class':'form-control'}),
        #            "city":forms.TextInput(attrs={'placeholder':'City','class':'form-control'}),
        #            "mobile_number":forms.TextInput(attrs={'placeholder':'Mobile Number','class':'form-control'}),
        #            "postal_code":forms.TextInput(attrs={'placeholder':'Postal Code','class':'form-control'}),
        #      }
