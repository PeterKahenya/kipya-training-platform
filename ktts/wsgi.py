import os
import sys

from django.core.wsgi import get_wsgi_application
# sys.path.append('/home/peter/projects/ktts')
# sys.path.append('/home/peter/projects/ktts/ktts')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ktts.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "ktts.settings"

application = get_wsgi_application()

