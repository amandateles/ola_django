from django.urls import path
from django.http import HttpResponse
from . import views 

def ola_django(request):
    return HttpResponse('Ola mundo, sou o Django!')

urlpatterns = [
    path('ola_django/', ola_django),
]