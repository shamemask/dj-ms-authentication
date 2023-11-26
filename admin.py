from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models2 here.

from authentication.UserModel import FizUser, UrUser
class CustomFizUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone', 'promo_code', 'terms_of_service', 'is_active')
    list_filter = ('is_active', 'promo_code', 'terms_of_service')
    search_fields = ('email', 'full_name', 'phone')
class CustomUrUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'form', 'phone', 'full_name', 'city', 'organization_name', 'legal_address', 'inn', 'kpp', 'bank', 'bik', 'account_number', 'correspondent_account', 'terms_of_service', 'is_active')
    search_fields = ('email', 'full_name', 'phone', 'organization_name')
    search_fields = ('is_active', 'terms_of_service')

try:
    # admin.site.unregister(FizUser)
    admin.site.register(FizUser, CustomFizUserAdmin)
except admin.sites.AlreadyRegistered:
    pass
try:
    # admin.site.unregister(UrUser)
    admin.site.register(UrUser, CustomUrUserAdmin)
except admin.sites.AlreadyRegistered:
    pass
