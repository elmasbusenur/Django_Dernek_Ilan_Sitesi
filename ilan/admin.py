from django.contrib import admin

# Register your models here.
from ilan.models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']  # hangi alanlar görülsün istiyorum categoride
    #readonly_fields = ('image_tag',)
    list_filter = ['status']  # statuye göre filtreliyorum
admin.site.register(Category, CategoryAdmin) #category bir model ve import ediyoruz