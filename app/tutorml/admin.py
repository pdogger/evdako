from django.contrib import admin

from .models import FAQ, Article, Choice, Dataset, Question, Subscription


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "category", "views", "pub_date")
    search_fields = ["title"]


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category')
    search_fields = ['name']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email", "notify_tutorials", "notify_datasets")
    search_fiels = ["email"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text',)
    search_fields = ['text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(FAQ)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Dataset, DatasetAdmin)
