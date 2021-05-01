from django.contrib import admin
from api.models import Manufacturer,Category,Prodcut,Comment
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Prodcut)
admin.site.unregister(Prodcut)
admin.site.unregister(Comment)
admin.site.unregister(Manufacturer)
admin.site.unregister(Category)

@admin.register(Prodcut)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "cost", "rating", "manufacturer", "category")

@admin.register(Manufacturer)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "main_field", "address")

@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Comment)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email", "content", "created")
    