from ilan.models import Ilan, Category, Images
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'} #menüyü kontrol etmek istediğim için page ekliyorum
    return render(request, 'index.html', context)
# contexte ekledik ve index html e gönderdik ve index html de istediğimiz yere istediğimiz bilgileri yazdık
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting} #setting gönderiyorum
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    if request.method == 'POST':  # form post edildi mi. edilmezse setting e iner.
        form = ContactFormu(request.POST)  # CONTACT FORMUNU POSTLA EŞLEŞTİR
        if form.is_valid(): #form geçerliyse dataya aktar eşleştir
            data = ContactFormMessage() #model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarıyla gönderilmiştir. Teşekkür Ederiz")
            return HttpResponseRedirect('/iletisim')  # formu iletişim sayfasına gönderiyoruz
#forma ulaşmak için yukarısıda kaydetmek için
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()  # contact formu çağrıyoruz
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)  # iletişim sayfasına formu gönderiyoruz
