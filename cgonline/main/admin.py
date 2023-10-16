from django.contrib import admin

from .models import (
    ContactLink,
    ContactMessage,
    Question,
    Friend,
    Presentation,
    TitleText,
)

# Register your models here.
admin.site.register(Question)
admin.site.register(Friend)
admin.site.register(ContactMessage)
admin.site.register(ContactLink)
admin.site.register(Presentation)
admin.site.register(TitleText)
