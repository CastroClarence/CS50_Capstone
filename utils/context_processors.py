from mysite.models import Service, Inquiry

def get_unread(request):
    user = request.user
    count = 0
    inquiries_unread = Inquiry.objects.filter(service__user=user, read=False)
    if user.is_authenticated:
        services = Service.objects.filter(user = user)
        for service in services:
            inquiries = Inquiry.objects.filter(service = service)
            for inquiry in inquiries:
                if inquiry.read == False:
                    count+=1
    
    return {
        'inquiry_unread_count' : count,
        'inquiries_unread' : inquiries_unread
    }