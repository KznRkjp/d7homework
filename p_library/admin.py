from django.contrib import admin

# Register your models here.


from p_library.models import Book, Author, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

# @admin.register(Publisher)
# class PublisherAdmin(admin.ModelAdmin):
#     pass
