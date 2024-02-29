from django.db import models


class Employee(models.Model):
    class Level(models.TextChoices):
        JUNIOR = "junior"
        MIDDLE = "middle"
        SENIOR = "senior"

    name = models.CharField(max_length=100, verbose_name="Имя")
    second_name = models.CharField(max_length=100, verbose_name="Фамилия")
    role = models.CharField(max_length=500, verbose_name="Должность")
    level = models.CharField(max_length=6,
                             choices=Level.choices,
                             default=Level.JUNIOR,
                             verbose_name='Грейд')

    def __str__(self):
        return f"{self.second_name} {self.name} - {self.role} ({self.level})"
