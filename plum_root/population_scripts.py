import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plum_site.settings')

import django
django.setup()

#fake pop script
import random
from quotes.models import Quotes
from faker import Faker

fakegen = Faker()
