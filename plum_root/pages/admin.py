from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)


#username: plumadmin
#email: plum@admin.com
#password: django.contrib
# Register your models here.
admin.site.register(Page, PageAdmin)