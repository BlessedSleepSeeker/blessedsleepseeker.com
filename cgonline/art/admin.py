from django.contrib import admin

from .models import Album, Piece

# Register your models here.
admin.site.register(Piece)
admin.site.register(Album)
