from django.contrib import admin
from .models import PPT
@admin.register(PPT)
class PPTAdmin(admin.ModelAdmin):
    list_display = ["ppt","status","created_at","ppt_name","ppt_modified"]
    search_fields = [
        "status",
        "created_at",
    ]
    readonly_fields = ["created_at"]
    list_per_page = 10
    list_max_show_all = 100 
