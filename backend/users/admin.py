from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'pk',
        'email', 'password',
        'first_name', 'last_name',
        'subscriber_count', 'recipes_count'
    )
    list_editable = ('password', )
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    empty_value_display = '-пустота-'

    @admin.display(description='Количество подписчиков')
    def subscriber_count(self, obj):
        return obj.subscriber.count()
    
    @admin.display(description='Количество рецептов')
    def recipes_count(self, obj):
        return obj.recipes_count.count()
    



@admin.register(models.Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    list_editable = ('user', 'author')
    empty_value_display = '-пустота-'
