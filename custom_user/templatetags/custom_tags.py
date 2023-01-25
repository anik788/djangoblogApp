from django import template
from custom_user.models import UserProfile

register = template.Library()


@register.simple_tag()
def get_profile_id(user_id=None):
    profile_id = UserProfile.objects.filter(user_id=user_id).first()
    if profile_id:
        return profile_id.id
    return 0
