from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Seller, SpecialSale, Laptop, Phone, PreBuiltPC, Monitor, ExternalHardDrive, Keyboard

from .forms import SellerForm, SpecialSaleForm, LaptopForm, PhoneForm, PreBuiltPCForm, MonitorForm, \
    ExternalHardDriveForm, KeyboardForm

from django.urls import reverse_lazy

from django.db.models import Q, F

from django.views.generic import CreateView
from .forms import SignUpForm


# done
class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')


# done
class UserLogoutView(LogoutView):
    redirect_authenticated_user = True
    next_page = reverse_lazy('login')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"


# done
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')


class GetPhone(LoginRequiredMixin, ListView):
    model = Phone
    template_name = "home.html"

    def get_queryset(self):
        ram = self.request.GET.get("ram")
        price = self.request.GET.get("price")
        object_list = Seller.objects.filter(
            Q(ram__gte=ram) & Q(price__lte=price)
        )
        return object_list


class GetSortByPrice(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = "injash ro shoma ok konid"

    def get_queryset(self):
        object_list = Seller.objects.order_by('-sold')
        return object_list


class UpdatePhonesOffer(LoginRequiredMixin, ListView):
    model = Phone
    template_name = "injash ro shoma ok konid"

    def get_queryset(self):
        object_list = Seller.objects.filter(Q(spc_sale__discount__gte=5) & Q(spc_sale__discount__lte=10)) \
            .update(price=((F('price') * F('spc_sale__discount')) / 100))
        return object_list


class AveragePriceOfMonitor(LoginRequiredMixin, ListView):
    model = Monitor
    template_name = "inja ro shoma ok konid"

    def get_queryset(self):
        display_size = self.request.GET.get("display_size")
        brand = self.request.GET.get("brand")
        object_list = Monitor.objects.filter(
            Q(display_size__gte=display_size) & Q(brand=brand)
        )
        return object_list


class Update20Percent(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = "inja ro shoma ok konid"

    def get_queryset(self):
        object_list = Laptop.objects.filter(quantity=1).update(price=(F('price') * 20) / 100)
        return object_list


# done
class SellerSearchView(LoginRequiredMixin, ListView):
    model = Seller
    template_name = "seller/sellers.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class SellerListView(LoginRequiredMixin, ListView):
    model = Seller
    template_name = "seller/sellers.html"


# done
class SellerDetailView(LoginRequiredMixin, DetailView):
    model = Seller
    template_name = "seller/detail.html"


# done
class SellerCreateView(LoginRequiredMixin, CreateView):
    model = Seller
    template_name = "seller/create.html"
    form_class = SellerForm
    success_url = reverse_lazy('seller_list')


# done
class SellerUpdateView(LoginRequiredMixin, UpdateView):
    model = Seller
    template_name = "seller/update.html"
    fields = '__all__'
    success_url = reverse_lazy('seller_list')


# done
class SellerDeleteView(LoginRequiredMixin, DeleteView):
    model = Seller
    template_name = "seller/delete.html"
    success_url = reverse_lazy('seller_list')


# done
class SpecialSaleListView(LoginRequiredMixin, ListView):
    model = SpecialSale
    template_name = "specialsale/special_sales.html"


# done
class SpecialSaleDetailView(LoginRequiredMixin, DetailView):
    model = SpecialSale
    template_name = "specialsale/detail.html"


# done
class SpecialSaleCreateView(LoginRequiredMixin, CreateView):
    model = SpecialSale
    template_name = "specialsale/create.html"
    form_class = SpecialSaleForm
    success_url = reverse_lazy('special_sale_list')


# done
class SpecialSaleUpdateView(LoginRequiredMixin, UpdateView):
    model = SpecialSale
    template_name = "specialsale/update.html"
    fields = '__all__'
    success_url = reverse_lazy('special_sale_list')


# done
class SpecialSaleDeleteView(LoginRequiredMixin, DeleteView):
    model = SpecialSale
    template_name = "specialsale/delete.html"
    success_url = reverse_lazy('special_sale_list')


# done
class SpecialSaleSearchView(LoginRequiredMixin, ListView):
    model = SpecialSale
    template_name = "specialsale/special_sales.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(sales_name__icontains=name)
        return object_list


# done
class LaptopSearchView(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = "laptop/laptops.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class LaptopListView(LoginRequiredMixin, ListView):
    model = Laptop
    template_name = "laptop/laptops.html"


# done
class LaptopDetailView(LoginRequiredMixin, DetailView):
    model = Laptop
    template_name = "laptop/detail.html"


# done
class LaptopCreateView(LoginRequiredMixin, CreateView):
    model = Laptop
    template_name = "laptop/create.html"
    form_class = LaptopForm
    success_url = reverse_lazy('laptop_list')


# done
class LaptopUpdateView(LoginRequiredMixin, UpdateView):
    model = Laptop
    template_name = "laptop/update.html"
    fields = '__all__'
    success_url = reverse_lazy('laptop_list')


# done
class LaptopDeleteView(LoginRequiredMixin, DeleteView):
    model = Laptop
    template_name = "laptop/delete.html"
    success_url = reverse_lazy('laptop_list')


# done
class PhoneListView(LoginRequiredMixin, ListView):
    model = Phone
    template_name = "phone/phones.html"


# done
class PhoneDetailView(LoginRequiredMixin, DetailView):
    model = Phone
    template_name = "phone/detail.html"


# done
class PhoneCreateView(LoginRequiredMixin, CreateView):
    model = Phone
    template_name = "phone/create.html"
    form_class = PhoneForm
    success_url = reverse_lazy('phone_list')


# done
class PhoneUpdateView(LoginRequiredMixin, UpdateView):
    model = Phone
    template_name = "phone/update.html"
    fields = '__all__'
    success_url = reverse_lazy('phone_list')


# done
class PhoneDeleteView(LoginRequiredMixin, DeleteView):
    model = Phone
    template_name = "phone/delete.html"
    success_url = reverse_lazy('phone_list')


# done
class PhoneSearchView(LoginRequiredMixin, ListView):
    model = Phone
    template_name = "phone/phones.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class PreBuiltPCListView(LoginRequiredMixin, ListView):
    model = PreBuiltPC
    template_name = "prebuiltpc/prebuiltpcs.html"


# done
class PreBuiltPCDetailView(LoginRequiredMixin, DetailView):
    model = PreBuiltPC
    template_name = "prebuiltpc/detail.html"


# done
class PreBuiltPCCreateView(LoginRequiredMixin, CreateView):
    model = PreBuiltPC
    template_name = "prebuiltpc/create.html"
    form_class = PreBuiltPCForm
    success_url = reverse_lazy('pre_built_pc_list')


# done
class PreBuiltPCUpdateView(LoginRequiredMixin, UpdateView):
    model = PreBuiltPC
    template_name = "prebuiltpc/update.html"
    fields = '__all__'
    success_url = reverse_lazy('pre_built_pc_list')


# done
class PreBuiltPCDeleteView(LoginRequiredMixin, DeleteView):
    model = PreBuiltPC
    template_name = "prebuiltpc/delete.html"
    success_url = reverse_lazy('pre_built_pc_list')


# done
class PreBuiltPCSearchView(LoginRequiredMixin, ListView):
    model = PreBuiltPC
    template_name = "prebuiltpc/prebuiltpcs.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class MonitorListView(LoginRequiredMixin, ListView):
    model = Monitor
    template_name = "monitor/monitors.html"


# done
class MonitorDetailView(LoginRequiredMixin, DetailView):
    model = Monitor
    template_name = "monitor/detail.html"


# done
class MonitorCreateView(LoginRequiredMixin, CreateView):
    model = Monitor
    template_name = "monitor/create.html"
    form_class = MonitorForm
    success_url = reverse_lazy('monitor_list')


# done
class MonitorUpdateView(LoginRequiredMixin, UpdateView):
    model = Monitor
    template_name = "monitor/update.html"
    fields = '__all__'
    success_url = reverse_lazy('monitor_list')


# done
class MonitorDeleteView(LoginRequiredMixin, DeleteView):
    model = Monitor
    template_name = "Monitor/delete.html"
    success_url = reverse_lazy('monitor_list')


# done
class MonitorSearchView(LoginRequiredMixin, ListView):
    model = Monitor
    template_name = "monitor/monitors.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class ExternalHardDriveListView(LoginRequiredMixin, ListView):
    model = ExternalHardDrive
    template_name = "externalharddrive/externalharddrives.html"


# done
class ExternalHardDriveDetailView(LoginRequiredMixin, DetailView):
    model = ExternalHardDrive
    template_name = "externalharddrive/detail.html"


# done
class ExternalHardDriveCreateView(LoginRequiredMixin, CreateView):
    model = ExternalHardDrive
    template_name = "externalharddrive/create.html"
    form_class = ExternalHardDriveForm
    success_url = reverse_lazy('external_hard_drive_list')


# done
class ExternalHardDriveUpdateView(LoginRequiredMixin, UpdateView):
    model = ExternalHardDrive
    template_name = "externalharddrive/update.html"
    fields = '__all__'
    success_url = reverse_lazy('external_hard_drive_list')


# done
class ExternalHardDriveDeleteView(LoginRequiredMixin, DeleteView):
    model = ExternalHardDrive
    template_name = "externalharddrive/delete.html"
    success_url = reverse_lazy('external_hard_drive_list')


# done
class ExternalHardDriveSearchView(LoginRequiredMixin, ListView):
    model = ExternalHardDrive
    template_name = "externalharddrive/externalharddrives.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list


# done
class KeyboardListView(LoginRequiredMixin, ListView):
    model = Keyboard
    template_name = "keyboard/keyboards.html"


# done
class KeyboardDetailView(LoginRequiredMixin, DetailView):
    model = Keyboard
    template_name = "keyboard/detail.html"


# done
class KeyboardCreateView(LoginRequiredMixin, CreateView):
    model = Keyboard
    template_name = "keyboard/create.html"
    form_class = KeyboardForm
    success_url = reverse_lazy('keyboard_list')


# done
class KeyboardUpdateView(LoginRequiredMixin, UpdateView):
    model = Keyboard
    template_name = "keyboard/update.html"
    fields = '__all__'
    success_url = reverse_lazy('keyboard_list')


# done
class KeyboardDeleteView(LoginRequiredMixin, DeleteView):
    model = Keyboard
    template_name = "keyboard/delete.html"
    success_url = reverse_lazy('keyboard_list')


# done
class KeyboardSearchView(LoginRequiredMixin, ListView):
    model = Keyboard
    template_name = "keyboard/keyboards.html"

    def get_queryset(self):
        name = self.request.GET.get("name")
        object_list = self.model.objects.all()
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        return object_list
