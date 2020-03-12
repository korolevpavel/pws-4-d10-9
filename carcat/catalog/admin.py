from django.contrib import admin
from .models import Car, Color, Producer

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass


