from .models import Notifications

def notification_data(request):
    unread_notifications = Notifications.objects.filter(read_status=False).order_by('-created_at')[:5]
    unread_count = Notifications.objects.filter(read_status=False).count()

    return {
        'notifications': unread_notifications,
        'unread_count': unread_count,
    }
