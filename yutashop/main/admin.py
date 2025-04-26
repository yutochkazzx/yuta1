from django.contrib import admin
from .models import Category, Size,ClothingItems, ClothingItemSize



class ClothinItemSizeInLine(admin.TabularInline):
    model = ClothingItemSize
    extra = 4


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name',)

@admin.register(ClothingItems)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','category',
                    'available', 'price', 'discount',
                    'created_at','updated_at')
    list_filter = ('available', 'category')
    prepopulated_fields = {'slug':('name',)}
    ordering =  ['-created_at',]
    inlines = [ClothinItemSizeInLine]

