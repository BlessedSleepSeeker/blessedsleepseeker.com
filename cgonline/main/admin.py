from django.contrib import admin

from .models import ContactOption, FAQuestion, Friend

# Register your models here.
admin.site.register(FAQuestion)
admin.site.register(Friend)
admin.site.register(ContactOption)
