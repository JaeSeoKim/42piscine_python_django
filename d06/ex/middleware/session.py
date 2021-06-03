from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time
import random


SESSION_EXFIRE_TIME = 42
SESSION_TIMEOUT_KEY = "_session_anonmymous_timestamp_"


class AnonymousSessionMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.user.is_authenticated:
            return

        init_time = request.session.setdefault(
            SESSION_TIMEOUT_KEY, time.time())

        session_is_expired = time.time() - init_time > SESSION_EXFIRE_TIME

        if session_is_expired:
            request.session.flush()

        request.session.setdefault('anonymous', random.choice(
            settings.ANONYMOUS_NAMES))

        request.user.username = request.session.get('anonymous')
