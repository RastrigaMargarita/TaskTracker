from rest_framework import serializers

from employees.models import Employee
from tasks.models import Task
from tasks.serializers.task import DependedTasksSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CurrentWorksSerializer(serializers.ModelSerializer):
    task_quantity = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    task_list = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ("employee", "task_quantity", "task_list")

    def get_task_quantity(self, instance):

        return Task.objects\
            .filter(responsible_person=instance,
                    status=Task.TaskStatus.TAKEN)\
            .count()

    def get_task_list(self, instance):

        return DependedTasksSerializer(Task.objects
                                       .filter(responsible_person=instance)
                                       .exclude(status=Task.TaskStatus.DONE),
                                       many=True, read_only=True).data

    def get_employee(self, instance):
        return str(instance)
