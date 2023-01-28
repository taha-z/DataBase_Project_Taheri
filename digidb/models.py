from django.db import models
from django.urls import reverse


# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=1, default="")
    phone_number = models.CharField(max_length=100, blank=1, default="")
    address = models.TextField(blank=1, default="")

    def __str__(self):
        return f"seller : {self.name}"


class SpecialSale(models.Model):
    sales_name = models.CharField(max_length=100)
    discount = models.PositiveBigIntegerField()
    starting_date = models.DateField(blank=1, default="2023-01-01")
    ending_date = models.DateField(blank=1, default="2023-01-01")

    def __str__(self):
        return f"froosh vijhe : {self.sales_name} takhfif : {self.discount}%"


class AbstractProduct(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=1, default="")
    weight = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    sold = models.PositiveBigIntegerField()
    spc_sale = models.ForeignKey(SpecialSale, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)


class Laptop(AbstractProduct):
    display_size = models.PositiveSmallIntegerField()
    ram = models.PositiveSmallIntegerField()
    cpu = models.PositiveSmallIntegerField()
    storage = models.PositiveSmallIntegerField()
    graphic_card = models.CharField(max_length=100, blank=1, default="")

    def __str__(self):
        return f"laptop : {self.name} brand : {self.brand}"


class Phone(AbstractProduct):
    display_size = models.PositiveSmallIntegerField()
    ram = models.PositiveSmallIntegerField()
    cpu = models.PositiveSmallIntegerField()
    storage = models.PositiveSmallIntegerField()
    os = models.CharField(max_length=100, blank=1, default="")

    def __str__(self):
        return f"phone : {self.name} brand : {self.brand}"


class PhoneCover(AbstractProduct):
    model = models.CharField(max_length=100)
    magnet = models.BooleanField(blank=1, default=0)

    def __str__(self):
        return f"phone cover : {self.name} brand : {self.brand}"


class PhonePowerBank(AbstractProduct):
    capacity = models.PositiveSmallIntegerField(blank=1, default=1)
    ports = models.PositiveSmallIntegerField(blank=1, default=1)
    fast_charge = models.BooleanField(blank=1, default=0)

    def __str__(self):
        return f"phone power bank : {self.name} brand : {self.brand}"


class PhoneHolder(AbstractProduct):
    rotation = models.BooleanField(blank=1, default=0)

    def __str__(self):
        return f"phone holder : {self.name} brand : {self.brand}"


class Monitor(AbstractProduct):
    display_size = models.PositiveSmallIntegerField()
    refresh_rate = models.PositiveSmallIntegerField(blank=1, default=1)
    inputs = models.PositiveSmallIntegerField(blank=1, default=1)

    def __str__(self):
        return f"monitor : {self.name} brand : {self.brand}"


class Keyboard(AbstractProduct):
    class TypeChoices(models.TextChoices):
        mechanical = "M", "Mechanical"
        ducky = "D", "Ducky"

    rgb = models.BooleanField(blank=1, default=0)
    type = models.CharField(max_length=10, choices=TypeChoices.choices, blank=1, default="")
    acuuracy_range = models.PositiveSmallIntegerField(blank=1, default=1)


class PreBuiltPC(AbstractProduct):
    ram = models.PositiveSmallIntegerField()
    cpu = models.PositiveSmallIntegerField()
    storage = models.PositiveSmallIntegerField()
    graphic_card = models.CharField(max_length=100, blank=1, default="")

    def __str__(self):
        return f"pre built pc : {self.name} brand : {self.brand}"


class ExternalHardDrive(AbstractProduct):
    class TypeChoices(models.TextChoices):
        ssd = "S", "SSD"
        hdd = "H", "HDD"

    hard_type = models.CharField(max_length=10, choices=TypeChoices.choices, blank=1, default="")
    capacity = models.PositiveSmallIntegerField(blank=1, default=1)
    transfer_rate = models.PositiveSmallIntegerField(blank=1, default=1)
