from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
admin.sites.site.register(Post)
admin.sites.site.register(Comment)
