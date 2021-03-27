from django.core.management import BaseCommand
from mimesis.schema import Field, Schema

from library.models import Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--iterations',
                            type=int,
                            action='store')

    def handle(self, *args, **options):
        Author.objects.all().delete()
        _ = Field('en')
        description = (
            lambda: {
                'uuid': _('uuid'),
                'first_name': _('person.first_name'),
                'last_name': _('person.last_name'),
                'birthday_year': _('datetime.year', minimum=1950, maximum=2000)
            }
        )
        schema = Schema(schema=description)
        data_list = list(schema.create(iterations=options['iterations']))
        for obj in data_list:
            Author.objects.create(**obj)
