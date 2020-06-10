import json, os

from django.core.management.base import BaseCommand
from articles.models import Article
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'articles.json'), 'r') as json_file:
            data = json.load(json_file)

            for fields in data:
                pk = fields['pk']

                field = fields['fields']
                title = field['title']
                text = field['text']
                published_at = field['published_at']
                image = field['image']

                Article.objects.create(id=pk, title=title, text=text, published_at=published_at,
                                     image=image)