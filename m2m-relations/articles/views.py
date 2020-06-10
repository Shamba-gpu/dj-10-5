from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    articles = Article.objects.all().prefetch_related('scopes').order_by(ordering)
    for article in articles:
        for scope in article.scopes.all():
            attrs = scope.article_tag_relation_set.get(article=article)
            scope.is_main = attrs.is_main

    context = {'object_list': articles}
    return render(request, template, context)
