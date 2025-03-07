from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
          list_display = ('text', 'pub_date', 'author', 'group')
          search_fields = ('text',)
          list_filter = ('pub_date',)
          list_editable = ('group',)
          empty_value_display = '-пусто'

class GroupAdmin(admin.ModelAdmin):
          #prepopulated_fields = {"slug": ('title',)}
          list_display = ("pk", "title", "slug")
          search_fields = ("title", "slug")
          #list_filter = ("slug")
          empty_value_display = '-пусто'

admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)