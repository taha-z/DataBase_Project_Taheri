"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from digidb.views import SellerListView, SellerDeleteView, SellerCreateView, SellerUpdateView, SellerDetailView, \
    SpecialSaleListView, SpecialSaleCreateView, SpecialSaleDeleteView, SpecialSaleUpdateView, SpecialSaleDetailView, \
    LaptopListView, LaptopCreateView, LaptopDeleteView, LaptopUpdateView, LaptopDetailView, \
    PhoneListView, PhoneCreateView, PhoneDeleteView, PhoneUpdateView, PhoneDetailView, \
    PreBuiltPCCreateView, PreBuiltPCListView, PreBuiltPCDeleteView, PreBuiltPCUpdateView, PreBuiltPCDetailView, \
    MonitorListView, MonitorCreateView, MonitorDeleteView, MonitorUpdateView, MonitorDetailView, \
    ExternalHardDriveCreateView, ExternalHardDriveUpdateView, ExternalHardDriveDeleteView, ExternalHardDriveDetailView, \
    ExternalHardDriveListView, KeyboardListView, KeyboardCreateView, KeyboardDeleteView, KeyboardUpdateView, \
    KeyboardDetailView, SellerSearchView, SpecialSaleSearchView, LaptopSearchView, PhoneSearchView, \
    PreBuiltPCSearchView, \
    MonitorSearchView, ExternalHardDriveSearchView, KeyboardSearchView, GetPhone, GetSortByPrice, AveragePriceOfMonitor, \
    Update20Percent, UpdatePhonesOffer, UserLoginView, UserLogoutView, SignUpView, HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    path("get_phone/", GetPhone.as_view()),
    path("get_sort_by_price/", GetSortByPrice.as_view()),
    path("average_price_monitor/", AveragePriceOfMonitor.as_view()),
    path("update_20_percent/", Update20Percent.as_view()),
    path("update_phone_offer/", UpdatePhonesOffer.as_view()),

    path("seller_search/", SellerSearchView.as_view(), name='seller_search'),
    path("seller_list/", SellerListView.as_view(), name='seller_list'),
    path("<int:pk>/seller_delete/", SellerDeleteView.as_view(), name='seller_delete'),
    path("seller_create/", SellerCreateView.as_view(), name='seller_create'),
    path("<int:pk>/seller_update/", SellerUpdateView.as_view(), name='seller_update'),
    path("<int:pk>/seller_detail/", SellerDetailView.as_view(), name='seller_detail'),

    path("special_sale_list_search/", SpecialSaleSearchView.as_view(), name='special_sale_search'),
    path("special_sale_list/", SpecialSaleListView.as_view(), name='special_sale_list'),
    path("<int:pk>/special_sale_delete/", SpecialSaleDeleteView.as_view(), name='special_sale_delete'),
    path("special_sale_create/", SpecialSaleCreateView.as_view(), name='special_sale_create'),
    path("<int:pk>/special_sale_update/", SpecialSaleUpdateView.as_view(), name='special_sale_update'),
    path("<int:pk>/special_sale_detail/", SpecialSaleDetailView.as_view(), name='special_sale_detail'),

    path("laptop_search/", LaptopSearchView.as_view(), name='laptop_search'),
    path("laptop_list/", LaptopListView.as_view(), name='laptop_list'),
    path("<int:pk>/laptop_delete/", LaptopDeleteView.as_view(), name='laptop_delete'),
    path("laptop_create/", LaptopCreateView.as_view(), name='laptop_create'),
    path("<int:pk>/laptop_update/", LaptopUpdateView.as_view(), name='laptop_update'),
    path("<int:pk>/laptop_detail/", LaptopDetailView.as_view(), name='laptop_detail'),

    path("phone_search/", PhoneSearchView.as_view(), name='phone_search'),
    path("phone_list/", PhoneListView.as_view(), name='phone_list'),
    path("<int:pk>/phone_delete/", PhoneDeleteView.as_view(), name='phone_delete'),
    path("phone_create/", PhoneCreateView.as_view(), name='phone_create'),
    path("<int:pk>/phone_update/", PhoneUpdateView.as_view(), name='phone_update'),
    path("<int:pk>/phone_detail/", PhoneDetailView.as_view(), name='phone_detail'),

    path("pre_built_pc_search/", PreBuiltPCSearchView.as_view(), name='pre_built_pc_search'),
    path("pre_built_pc_list/", PreBuiltPCListView.as_view(), name='pre_built_pc_list'),
    path("<int:pk>/pre_built_pc_delete/", PreBuiltPCDeleteView.as_view(), name='pre_built_pc_delete'),
    path("pre_built_pc_create/", PreBuiltPCCreateView.as_view(), name='pre_built_pc_create'),
    path("<int:pk>/pre_built_pc_update/", PreBuiltPCUpdateView.as_view(), name='pre_built_pc_update'),
    path("<int:pk>/pre_built_pc_detail/", PreBuiltPCDetailView.as_view(), name='pre_built_pc_detail'),

    path("monitor_search/", MonitorSearchView.as_view(), name='monitor_search'),
    path("monitor_list/", MonitorListView.as_view(), name='monitor_list'),
    path("<int:pk>/monitor_delete/", MonitorDeleteView.as_view(), name='monitor_delete'),
    path("monitor_create/", MonitorCreateView.as_view(), name='monitor_create'),
    path("<int:pk>/monitor_update/", MonitorUpdateView.as_view(), name='monitor_update'),
    path("<int:pk>/monitor_detail/", MonitorDetailView.as_view(), name='monitor_detail'),

    path("external_hard_drive_search/", ExternalHardDriveSearchView.as_view(), name='external_hard_drive_search'),
    path("external_hard_drive_list/", ExternalHardDriveListView.as_view(), name='external_hard_drive_list'),
    path("<int:pk>/external_hard_drive_delete/", ExternalHardDriveDeleteView.as_view(),
         name='external_hard_drive_delete'),
    path("external_hard_drive_create/", ExternalHardDriveCreateView.as_view(), name='external_hard_drive_create'),
    path("<int:pk>/external_hard_drive_update/", ExternalHardDriveUpdateView.as_view(),
         name='external_hard_drive_update'),
    path("<int:pk>/external_hard_drive_detail/", ExternalHardDriveDetailView.as_view(),
         name='external_hard_drive_detail'),

    path("keyboard_search/", KeyboardSearchView.as_view(), name='keyboard_search'),
    path("keyboard_list/", KeyboardListView.as_view(), name='keyboard_list'),
    path("<int:pk>/keyboard_delete/", KeyboardDeleteView.as_view(), name='keyboard_delete'),
    path("keyboard_create/", KeyboardCreateView.as_view(), name='keyboard_create'),
    path("<int:pk>/keyboard_update/", KeyboardUpdateView.as_view(), name='keyboard_update'),
    path("<int:pk>/keyboard_detail/", KeyboardDetailView.as_view(), name='keyboard_detail'),

]
