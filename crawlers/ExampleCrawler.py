# Set up environment for using the Django webapp model
from django.core.management import setup_environ
from webapp import settings
setup_environ(settings)

from webapp.ExampleApp.models import ExampleObject


def main():

    name = str(raw_input('name: '))
    value = str(raw_input('value: '))

    try:
        # Try to find an existing object with this name
        obj = ExampleObject.objects.get(name=name)

    except ExampleObject.DoesNotExist:
        obj = ExampleObject()

    finally:
        obj.name = name
        obj.value = value
        obj.save()


if __name__ == '__main__':
    main()

