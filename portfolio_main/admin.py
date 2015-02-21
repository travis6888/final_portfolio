from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag, MetaField, Author

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(MetaField)
admin.site.register(Author)