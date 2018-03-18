from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Review", {"fields": ["title", "authors"]}),
        ("review", {"fields": ["is_favorite", "review", "reviewed_by", "date_review"]}),
    ]
    readonly_fields = ("date_review",)

    def book_authors(self, obj):
        return obj.list_author()

    book_authors.short_description = "Author(s)"
    list_display = ("title", "book_authors", "date_review", "is_favorite")
    list_editable = ("is_favorite",)
    list_display_links = ('title', 'date_review')
    list_filter = ('is_favorite',)
    search_fields = ("title", 'authors__name',)


# Register your models here.
admin.site.register(Author)
