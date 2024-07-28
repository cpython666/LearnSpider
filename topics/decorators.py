from django.http import JsonResponse

def require_ua(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_agent = request.META.get('HTTP_USER_AGENT')
        if not user_agent:
            return JsonResponse({'error': 'User-Agent header is required'}, status=400)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
