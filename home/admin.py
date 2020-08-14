from django.contrib import admin

# Register your models here.
# home/models deki clasın migrations dan sonra çalışabilmesi için register yapmalıyız.
from home.models import Setting, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']  # statuse göre filtreleme olucak


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)