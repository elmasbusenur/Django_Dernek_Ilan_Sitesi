#ana urls nin içine bu dosyayı tanıttım.
#path('home/', include('home.urls')), #home/ gelen her şey home a ait olacak
from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'), #herhangi bir parametre girilmezse '' indexi görsün

]
