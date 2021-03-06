# Django
from braces.views import JSONResponseMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.list import ListView

# Third party
from persistent_messages.models import Message

# AstroBin
from astrobin.models import UserProfile

# This app
from astrobin_apps_notifications.utils import clear_notifications_template_cache, push_notification


class TestNotificationView(View):
    def post(request, *args, **kwargs):
        push_notification(
            [UserProfile.objects.get(user__username = kwargs.pop('username')).user],
            'test_notification',
            {})
        return HttpResponse("test_notification sent")


class NotificationListView(ListView):
    model = Message
    template_name = "astrobin_apps_notifications/all.html"
    context_object_name = "notification_list"

    def get_queryset(self):
        return Message.objects\
            .filter(user = self.request.user)\
            .order_by('read', '-created')


class NotificationMarkAllAsReadView(View):
    def post(self, request, *args, **kwargs):
        Message.objects.filter(user = request.user).update(read = True)
        clear_notifications_template_cache(request.user.username)
        return redirect(request.POST.get('next', '/'))


class NotificationClearTemplateCacheAjaxView(JSONResponseMixin, View):
    model = Message
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print self.request.user.username
            clear_notifications_template_cache(request.user.username)
            return self.render_json_response({'result': 'ok'})
        return HttpResponseForbidden()
