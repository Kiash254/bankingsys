from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title="admin panel"
admin.site.site_header="admin panel"



admin.site.register(Customer)