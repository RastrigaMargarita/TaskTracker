from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views import RegisterView

urlpatterns = [path('', RegisterView.as_view(template_name="users/register.html"), name='user')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
