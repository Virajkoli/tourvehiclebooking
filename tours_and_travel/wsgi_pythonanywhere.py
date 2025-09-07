# PythonAnywhere WSGI Configuration
import os
import sys

# Add your project directory to sys.path
project_home = '/home/yourusername/tours_and_travel'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'tours_and_travel.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
