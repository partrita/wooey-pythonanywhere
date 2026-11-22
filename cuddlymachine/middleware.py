__author__ = 'chris'
import sys
import traceback

from django.utils.deprecation import MiddlewareMixin


class ProcessExceptionMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code != 200:
            try:
                sys.stderr.write('{}'.format(''.join(traceback.format_exc())))
            except AttributeError:
                pass
        return response