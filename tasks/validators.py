from datetime import datetime, timezone
from rest_framework import serializers


def validate_deadline(value):
    if value < datetime.now(tz=timezone.utc).date():
        raise serializers.ValidationError("Дедлайн не может быть меньше текущего момента")
