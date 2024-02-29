
from django.urls import path
from rest_framework import routers

from employees.views.employee import EmployeeViewSet, CurrentWorksList

urlpatterns = [
    path('task/current_works', CurrentWorksList.as_view()),
]

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename="employee")
urlpatterns += router.urls
