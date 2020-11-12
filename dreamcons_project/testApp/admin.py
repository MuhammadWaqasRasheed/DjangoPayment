from django.contrib import admin

# Register your models here.

from .models import Pizza,Topping,Car,Manufacturer,Person,Group,Membership
"""
admin.site.register(Project)
admin.site.register(Task)
"""

admin.site.register(Pizza)
admin.site.register(Topping)

#foreign key tables
admin.site.register(Car)
admin.site.register(Manufacturer)

#manay to many field tables
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)