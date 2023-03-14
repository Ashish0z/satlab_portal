from django.contrib import admin
from .models import Form, LeaveForm, FineSheetForm, InventoryForm

admin.site.register(LeaveForm)
admin.site.register(FineSheetForm)
admin.site.register(InventoryForm)
