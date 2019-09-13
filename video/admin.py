from django.contrib import admin
from .models import Comment, Video


class Comment_Inline(admin.StackedInline):
    readonly_fields = ['text', 'date']
    model = Comment
    extra = 2


class Video_admin(admin.ModelAdmin):
    inlines = [Comment_Inline]
    readonly_fields = ['like']
    prepopulated_fields = {'slug' : ['name']}


admin.site.register(Video, Video_admin)




# Register your models here.
