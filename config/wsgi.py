"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import time
import threading
import requests

from django.core.wsgi import get_wsgi_application
from milkboy.views import auto_reply

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

application = get_wsgi_application()


def always():
    while True:
        while True:
            requests.get("https://www.milkboy-core-ai.tech/milkboy/tweet")
            # if req.status_code == requests.codes.ok:
            break
            # time.sleep(20)
        print('tried to access')
        time.sleep(3600)


t = threading.Thread(target=always)
t2 = threading.Thread(target=auto_reply)
t.start()
t2.start()
