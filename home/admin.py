from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Comment)
admin.site.register(Blog)