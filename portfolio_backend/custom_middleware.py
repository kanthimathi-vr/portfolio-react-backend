# portfolio_backend/custom_middleware.py
from django.utils.deprecation import MiddlewareMixin

class DisableCsrfMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/api/contact/':
            request.csrf_processing_done = True