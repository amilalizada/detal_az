from django.contrib import admin
from main.models import *

# admin.site.register(Tours)
admin.site.register(Marka)
admin.site.register(Modell)
admin.site.register(WishList)


# class TourImageInline(admin.TabularInline):
#     model = TourImages
#     extra = 3

# @admin.register(Tours)
# class RestaurantAdmin(admin.ModelAdmin):
#     inlines = [ TourImageInline, ]

