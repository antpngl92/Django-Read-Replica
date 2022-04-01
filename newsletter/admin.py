from django.contrib import admin

from newsletter.models import Article, Newsletter, Reporter


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'reporter')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', )
