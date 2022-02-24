import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'problems.settings')

import django

django.setup()


from demo.models import Course

print(Course.objects.all())
