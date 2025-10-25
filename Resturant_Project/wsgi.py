import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # <- keep it this way only if settings.py is in the same folder as wsgi.py

application = get_wsgi_application()

