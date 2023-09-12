from django.contrib import admin

from .models import ContactOption, Question, Friend, Presentation

# Register your models here.
admin.site.register(Question)
admin.site.register(Friend)
admin.site.register(ContactOption)
admin.site.register(Presentation)
