from django.contrib.auth import get_user_model

from domum import const
from users.models import AdminSettings


def domum(request):
    context = {}

    # Get superuser
    User = get_user_model()
    superuser = User.objects.filter(is_superuser=True)
    if superuser:
        admin_settings = AdminSettings.objects.get(user=superuser.first())

    return {
        "house_name": admin_settings.house_name if superuser else const.NAME,
        "const": const
    }