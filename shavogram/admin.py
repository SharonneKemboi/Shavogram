from django.contrib import admin
from .models import Photo, Comments,Follow,Profile

# Register your models here.
admin.site.register(Photo)
admin.site.register(Comments)
admin.site.register(Follow)
admin.site.register(Profile)