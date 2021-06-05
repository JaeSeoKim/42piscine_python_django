from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse


class LastArticleMiddlware(MiddlewareMixin):
    def process_response(self, request: HttpRequest, response: HttpResponse):
        # TODO: Context에 article 삽입 필요!
        return response
