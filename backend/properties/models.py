f
# added by shiv

from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

class Property(models.Model):
    address = models.CharField(max_length=255)
    built_year = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, related_name="properties")
    is_public = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="properties/", blank=True)

class Tenant(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="tenants")
    name = models.CharField(max_length=200)
    from_year = models.IntegerField(null=True, blank=True)
    to_year = models.IntegerField(null=True, blank=True)
