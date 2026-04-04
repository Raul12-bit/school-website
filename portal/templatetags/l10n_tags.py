from django import template
from django.utils import translation

register = template.Library()


@register.filter
def loc(obj, field_name: str):
    """Возвращает поле с учётом языка: name → name_ru / name_en при необходимости."""
    if obj is None:
        return ""
    lang = (translation.get_language() or "kk").split("-")[0]
    base = getattr(obj, field_name, None)
    if lang == "kk":
        return base if base is not None else ""
    alt = getattr(obj, f"{field_name}_{lang}", None)
    if alt:
        return alt
    return base if base is not None else ""
