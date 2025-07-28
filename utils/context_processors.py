from mysite.models import Service, Inquiry

def get_unread(request):
    user = request.user
    count = 0
    inquiries_read = Inquiry.objects.filter(service__user=user, read=True)
    inquiries_unread = Inquiry.objects.filter(service__user=user, read=False)
    inquiries_sent = Inquiry.objects.filter(user = user)
    if user.is_authenticated:
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