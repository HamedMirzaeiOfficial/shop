from django.contrib import admin
from shop.models import Product, Category, Comment, Image, Advertise, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ImageInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'active', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

    # update state of all chosen comments to active at once
    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image',
                    'created_on', 'updated', 'active')
    list_filter = ('created_on', 'updated', 'active')
    search_fields = ['title', 'body']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'email', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'message']
