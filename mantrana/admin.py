from django.contrib import admin
from .models import Services, Counsellors, FAQ

# Register your models here.

admin.site.register(Counsellors)
admin.site.register(Services)
admin.site.register(FAQ)