from django.core.management import BaseCommand
from mimesis.schema import Field, Schema

from usersapp.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--iterations',
                            type=int,
                            action='store')

    def handle(self, *args, **options):
        User.objects.all().delete()
        _ = Field('en')
        description = (
            lambda: {
                'uuid': _('uuid'),
                'username': _('text.word'),
                'password': _('person.password', length=12),
                'first_name': _('person.first_name'),
                'last_name': _('person.last_name'),
                'email': _('person.email', unique=True)
            }
        )
        schema = Schema(schema=description)
        data_list = list(schema.create(iterations=options['iterations']))
        for obj in data_list:
            User.objects.create(**obj)

        User.objects.create_superuser(
            username='super_admin',
            email='super@localhost',
            password='super_password',
            first_name='super',
            last_name='admin'
        )
