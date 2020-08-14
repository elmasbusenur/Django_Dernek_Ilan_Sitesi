from django.shortcuts import render
from home.models import Setting

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)
# contexte ekledik ve index html e gönderdik ve index html de istediğimiz yere istediğimiz bilgileri yazdık
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting} #menüyü kontrol etmek istediğim için page ekliyorum
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)