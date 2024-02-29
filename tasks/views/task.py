from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from tasks.models import Task
from tasks.paginations import PagePagination
from tasks.serializers.task import TaskSerializer, ImportantWorksSerializer


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('title')
    pagination_class = PagePagination

    def list(self, request, *args, **kwargs):

        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = TaskSerializer(paginated_queryset, many=True)
        data_to_return = self.get_paginated_response(serializer.data)
        return data_to_return


class ImportantWorksList(generics.ListAPIView):
    """Список важных задач: Поиск задач для распределения по сотрудникам в цепочке задач"""
    queryset = Task.objects\
        .filter(responsible_person__isnull=True, previouse_task__isnull=False)\
        .filter(previouse_task__responsible_person__isnull=False)

    serializer_class = ImportantWorksSerializer
