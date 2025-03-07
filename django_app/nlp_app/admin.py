from django.contrib import admin
from .models import Category, FormSending
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('id', 'clasificacion')

admin.site.register(Category, CategoriaAdmin)
admin.site.register(FormSending)

