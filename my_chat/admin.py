from django.contrib import admin

# Register your models here.
from my_chat.models import Online


@admin.register(Online)
class AdminOnline(admin.ModelAdmin):
    pass
