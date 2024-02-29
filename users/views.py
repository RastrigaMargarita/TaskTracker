from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import User


# Create your views here.
class RegisterView(CreateView):
    """Контроллер для регистрации пользователя"""
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:code')
