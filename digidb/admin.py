from django.contrib import admin

from .models import Seller, SpecialSale, AbstractProduct, Laptop, Phone, PhoneCover, PhonePowerBank, PhoneHolder, \
    Monitor, Keyboard, PreBuiltPC, ExternalHardDrive


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecialSale)
class SpecialSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneCover)
class PhoneCoverAdmin(admin.ModelAdmin):
    pass


@admin.register(PhonePowerBank)
class PhonePowerBankAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneHolder)
class PhoneHolderAdmin(admin.ModelAdmin):
    pass


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    pass

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    pass

@admin.register(PreBuiltPC)
class PreBuiltPCAdmin(admin.ModelAdmin):
    pass

@admin.register(ExternalHardDrive)
class ExternalHardDriveAdmin(admin.ModelAdmin):
    pass

