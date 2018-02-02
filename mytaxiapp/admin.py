from django.contrib import admin
from .models import (User, Driver, Car, Offer)


class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'email', 'first_name', 'last_name', 'year_of_birth', 'is_active', ]


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'color', ]


class DriverAdmin(admin.ModelAdmin):
    list_display = ['car', 'gender', 'experience', 'biography', 'is_active', ]


class OfferAdmin(admin.ModelAdmin):
    list_display = ['user', 'driver', 'start_place', 'finish_place', 'offer_price', ]


admin.site.register(User, UserAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Offer, OfferAdmin)