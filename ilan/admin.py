from django.contrib import admin

# Register your models here.
from ilan.models import Category, Ilan, Images

class IlanImageInline(admin.TabularInline):
    model = Images #images tablosuna ait olucak
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']  # hangi alanlar görülsün istiyorum categoride
    #readonly_fields = ('image_tag',)
    list_filter = ['status']  # statuye göre filtreliyorum

class IlanAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']  # hangi alanlar görülsün istiyorum categoride
    #readonly_fields = ('image_tag',)
    list_filter = ['status','category']  # statuye göre filtreliyorum
    inlines = [IlanImageInline]  # blogimagesinline ürün ekleme sırasında istiyorsam burayada bağlantısını kurmalıyım
    '''blogla ilgili olduğu için sadece onunla alakalı şeyleri ekler
imageye class ekliyorum'''

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','ilan','image']  # hangi alanlar görülsün istiyorum categoride
    #readonly_fields = ('image_tag',)
    #list_filter = ['status','category']  # statuye göre filtreliyorum

admin.site.register( Category, CategoryAdmin )  # category bir model ve import ediyoruz
admin.site.register( Ilan, IlanAdmin )
admin.site.register( Images, ImagesAdmin ) #resimlrin gözükmesi için imageadmin e bağlantı kuruyorum