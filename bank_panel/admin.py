from django.contrib import admin


from .models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'bank_info', 'bank_location', 'bank_phone', 'bank_email')

