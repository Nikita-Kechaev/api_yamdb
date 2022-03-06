from django.contrib import admin

from .models import Categorie, Genre, Review, Title, Comment

admin.site.register(Categorie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Title)
admin.site.register(Comment)
