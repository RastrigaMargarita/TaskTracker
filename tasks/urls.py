
from django.urls import path
from rest_framework import routers

from tasks.views.task import TaskViewSet, ImportantWorksList

urlpatterns = [

    path('important_works', ImportantWorksList.as_view()),
]

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename="task")
urlpatterns += router.urls
