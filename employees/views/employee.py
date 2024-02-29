from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from employees.models import Employee
from employees.serializers.employee import EmployeeSerializer, CurrentWorksSerializer


class EmployeeViewSet(ModelViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CurrentWorksList(generics.ListAPIView):
    """Список занятых сотрудников"""
    queryset = Employee.objects.all()
    serializer_class = CurrentWorksSerializer
