from mysite.models import Service, Inquiry

def get_unread(request):
    user = request.user
    count = 0
    if user.is_authenticated:
        services = Service.objects.filter(user = user)
        for service in services:
            inquiries = Inquiry.objects.filter(service = service)
            for inquiry in inquiries:
                if inquiry.read == False:
                    count+=1
    
    return {
        'inquiry_unread' : count
    }