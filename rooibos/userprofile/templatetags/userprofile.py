# commented out unused import
# import re
# from rooibos.contrib.tagging.models import Tag
# from rooibos.data.models import Record
# from rooibos.util.models import OwnedWrapper
# from django.utils.html import escape
# from django.template.loader import get_template
# from django.template import Context, Variable, Template
# from django.contrib.contenttypes.models import ContentType
from django import template
import json
from rooibos.userprofile.models import UserProfile
from rooibos.userprofile.views import load_settings

register = template.Library()

class ProfileSettingsNode(template.Node):
    def __init__(self, filter):
        self.filter = filter
    def render(self, context):
        user = context['request'].user if context.has_key('request') else None
        if user and user.is_authenticated():
            try:
                # TODO:  change from user.get_profile to user.profile (doesn't "just work")
                # (user.get_profile removed in django 1.7)
                #profile = user.get_profile()
                profile, created = UserProfile.objects.get_or_create(user=user)
            except UserProfile.DoesNotExist:
                profile = UserProfile.objects.create(user=user)
            if self.filter:
                preferences = profile.preferences.filter(setting__istartswith=self.filter)
            else:
                preferences = profile.preferences.all()
            settings = dict()
            for setting in preferences:
                settings[setting.setting] = setting.value
            result = json.dumps(settings)
        else:
            result = '{}';
        return result


@register.tag
def profile_settings(parser, token):
    try:
        tag_name, filter = token.contents.split(None, 1)
    except ValueError:
        tag_name = token.contents
        filter = None
    return ProfileSettingsNode(filter)


@register.filter
def profile_setting(user, setting):
    if user and user.is_authenticated():
        settings = load_settings(user, filter=setting)
        return settings.get(setting, [None])[0]
    else:
        return None
