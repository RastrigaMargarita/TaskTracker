from django.db import models

from tasks.validators import validate_deadline


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        NEW = "new"
        TAKEN = "TAKEN"
        DONE = "DONE"

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок")
    description = models.CharField(
        max_length=500,
        verbose_name="Описание")
    previouse_task = models.ForeignKey(
        "Task",
        on_delete=models.CASCADE,
        verbose_name="Предыдущий таск",
        blank=True,
        null=True)
    responsible_person = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        verbose_name="Ответственный",
        blank=True,
        null=True)
    status = models.CharField(
        max_length=5,
        choices=TaskStatus.choices,
        default=TaskStatus.NEW,
        verbose_name="Состояние")
    estimated_duration = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name="Оценка выполнения в часах")
    deadline = models.DateField(blank=True,
                                null=True, validators=[validate_deadline],
                                verbose_name="Срок выполнения")

    def __str__(self):
        return f"{self.title} - {self.estimated_duration}"
