#burada tablo oluşturulcak
from django.db import models

# Create your models here.
class Category(models.Model):  #model türümüz değişti
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100) #charfiels: uzunluk, alan türüdür.
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/') #buraya bir dosya eklenecek ve image olacak. upload eklenecek klasör adıdır.
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField() #adres satırında ürünü çağırabilmemiz için yazdığımız metin.adres satırında metinsel gördüğümüz şey
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)  # foreignkey self kendi id sine refere edicek, kendi kendine dönecek
                                #models.CASCADE silme işleminde ilişki kuruyor. bu silinirse ona bağlı şeylerde silinsin. cascade basamak demektir.
    create_at = models.DateTimeField(auto_now_add=True) #değişikliklerde tarih otomatik eklensin
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
