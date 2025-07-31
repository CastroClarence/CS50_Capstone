from mysite.models import Service, Inquiry, Bookmark, Support, User
from django.shortcuts import get_object_or_404

def get_inquiries(request):
    user = request.user
    count = 0
    if user.is_authenticated:
        inquiries_read = Inquiry.objects.filter(service__user=user, read=True)
        inquiries_unread = Inquiry.objects.filter(service__user=user, read=False)
        inquiries_sent = Inquiry.objects.filter(user = user)
        services = Service.objects.filter(user = user)
        for service in services:
            inquiries = Inquiry.objects.filter(service = service)
            for inquiry in inquiries:
                if inquiry.read == False:
                    count+=1
    
        return {
            'inquiry_unread_count' : count,
            'inquiries_unread' : inquiries_unread,
            'inquiries_read' : inquiries_read,
            'inquiries_sent' : inquiries_sent
        }
    return {}

def get_bookmarks(request):
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user = user)
        return {
            'bookmarks' : bookmarks
        }
    return {}

def get_supports(request):
    if request.user.is_authenticated:
        user = request.user
        supports = Support.objects.filter(user = user)
        return {
            'supports' : supports
        }
    return {}

def get_owner(request, **kwargs):
    if 'username' in kwargs:
        owner = get_object_or_404(User, username=kwargs['username'])
        return {
            'owner': owner
        }
    return {}

