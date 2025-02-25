# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    ) 
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# ...и регистрируем её в админке:
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)
