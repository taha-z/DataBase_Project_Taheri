from django import forms
from .models import Seller, SpecialSale, Laptop, Phone, PhoneCover, PhoneHolder, PhonePowerBank, PreBuiltPC, Monitor, \
    ExternalHardDrive, Keyboard
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            ]


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'


class SpecialSaleForm(forms.ModelForm):
    class Meta:
        model = SpecialSale
        fields = '__all__'


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'


class PhoneCoverForm(forms.ModelForm):
    class Meta:
        model = PhoneCover
        fields = '__all__'


class PhoneHolderForm(forms.ModelForm):
    class Meta:
        model = PhoneHolder
        fields = '__all__'


class PhonePowerBankForm(forms.ModelForm):
    class Meta:
        model = PhonePowerBank
        fields = '__all__'


class PreBuiltPCForm(forms.ModelForm):
    class Meta:
        model = PreBuiltPC
        fields = '__all__'


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'


class ExternalHardDriveForm(forms.ModelForm):
    class Meta:
        model = ExternalHardDrive
        fields = '__all__'


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'
