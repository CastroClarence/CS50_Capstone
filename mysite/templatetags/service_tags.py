from mysite.models import Bookmark, Support
from django import template
register = template.Library()
@register.filter
def is_bookmarked(service, user):
    bookmark = Bookmark.objects.filter(user = user, service = service, status = True)
    return bookmark.exists()

@register.filter
def is_supported(service, user):
    support = Support.objects.filter(user = user, service = service, status = True)
    return support.exists()