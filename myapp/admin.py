from django.contrib import admin
from . import models
from .models import Post,Comment,Contact


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','message']
    # list_editable = ['message']
    ordering = ['name', 'email']
    search_fields = ['name__istartswith','subject__istartswith']  


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content','post','user','time']
    ordering = ['content', 'post']
    search_fields = ['content', 'user__username', 'post__postname']
    

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['postname','category','user','time','likes','content']
    ordering = ['postname', 'category']


admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'
