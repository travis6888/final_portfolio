"""
WSGI config for formal_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formal_portfolio.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling
#
# application = Cling(get_wsgi_application())
# application = DjangoWhiteNoise(application)