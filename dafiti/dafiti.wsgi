import os, sys
sys.path.append('/home/dafiti/apps_wsgi')
sys.path.append('/home/dafiti/apps_wsgi/negociofacil')
os.environ['PYTHON_EGG_CACHE'] = '/home/dafiti/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'dafiti.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
