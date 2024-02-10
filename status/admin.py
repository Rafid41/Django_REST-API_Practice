# status\admin.py
from django.contrib import admin
from status.models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    #NOTE: table list page e j j field dekhate chai admin panel e seta ekhane likhbo
    list_display = ('text', 'created_at', 'user')
    
admin.site.register(Status, StatusAdmin)