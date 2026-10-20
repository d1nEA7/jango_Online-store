from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории и загружает тестовые из фикстуры'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixture',
            default='initial_data.json',
            help='Имя файла фикстуры в папке fixtures приложения catalog',
        )

    def handle(self, *args, **options):
        fixture_name = options['fixture']

        with transaction.atomic():
            # Продукты первыми — у них FK на категорию
            products_deleted, _ = Product.objects.all().delete()
            categories_deleted, _ = Category.objects.all().delete()

            self.stdout.write(self.style.WARNING(
                f'Удалено: продуктов={products_deleted}, категорий={categories_deleted}'
            ))

            call_command('loaddata', fixture_name, verbosity=0)

        self.stdout.write(self.style.SUCCESS(
            f'Загружено: категорий={Category.objects.count()}, '
            f'продуктов={Product.objects.count()}'
        ))