from django.contrib import admin

# Register your models here.
from familymembers.models import FamilyMember, Expenses

admin.site.register(FamilyMember)
admin.site.register(Expenses)
