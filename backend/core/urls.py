from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Historic Hammond project is alive!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # root URL now returns text
]
