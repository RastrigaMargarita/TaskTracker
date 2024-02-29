from django.db.models import Count
from rest_framework import serializers

from employees.models import Employee
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class DependedTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "estimated_duration", "deadline"]


class DependedEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["name", "second_name"]


class ImportantWorksSerializer(serializers.ModelSerializer):
    employees_to_assign = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["id", "title", "description", "deadline", "estimated_duration", "employees_to_assign"]

    def get_employees_to_assign(self, instance):
        # Сначала ищем занятость того сотрудника, который делает связаную задачу
        depended_employee_count = Task.objects \
            .filter(responsible_person=instance.previouse_task.responsible_person) \
            .exclude(status=Task.TaskStatus.DONE) \
            .count()

        if depended_employee_count <= 2:
            return DependedEmployeeSerializer(Employee.objects
                                              .filter(id=instance.previouse_task.responsible_person.id),
                                              many=True, read_only=True) \
                .data

        # Если он слишком занят, поищем, может есть совсем незанятый сотрудник"""
        all_employees = Employee.objects.all()
        for employee in all_employees.iterator():
            if not Task.objects \
                    .filter(responsible_person=employee) \
                    .exclude(status=Task.TaskStatus.DONE) \
                    .exists():
                return DependedEmployeeSerializer(Employee.objects
                                                  .filter(id=employee.id),
                                                  many=True, read_only=True) \
                    .data

        # Если все занятые, то ищем сотрудника у которого задач на 2 меньше чем у связанного сотрудника
        less_busy_employees = Task.objects \
                                  .filter(responsible_person__isNull=False) \
                                  .exclude(status=Task.TaskStatus.DONE) \
                                  .annotate(task_quantity=Count("responsible_person")) \
                                  .order_by("task_quantity")[:1]

        if less_busy_employees[0].task_quantity <= depended_employee_count - 2:
            return DependedEmployeeSerializer(
                Employee.objects
                .filter(id=less_busy_employees[0].responsible_person.id),
                many=True, read_only=True).data
        else:
            return DependedEmployeeSerializer(Employee.objects
                                              .filter(id=instance.previouse_task.responsible_person.id),
                                              many=True, read_only=True).data
