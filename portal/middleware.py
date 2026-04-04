from django.conf import settings
from django.utils import translation


def _language_explicitly_chosen(request):
    """Django 5.x сохраняет выбор языка в cookie (set_language), без LANGUAGE_SESSION_KEY."""
    return bool(request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME))


class KazakhDefaultLanguageMiddleware:
    """
    Пока нет cookie выбора языка — сайт на казахском (игнорируем Accept-Language браузера).
    После выбора в форме ставится LANGUAGE_COOKIE_NAME — работают ru/en.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not _language_explicitly_chosen(request):
            lang = settings.LANGUAGE_CODE
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
        return self.get_response(request)
