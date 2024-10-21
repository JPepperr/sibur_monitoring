from tortoise.models import Model
from tortoise import fields
from enum import Enum


class Problems(Model):
    class PriorityEnum(str, Enum):
        INFO = "INFO"
        CRIT = "CRIT"
        WARN = "WARN"

    class StatusEnum(str, Enum):
        START = "START"
        IN_PROGRESS = "IN_PROGRESS"
        END = "END"

    id = fields.IntField(null=False, pk=True, unique=True)
    priority = fields.CharEnumField(enum_type=PriorityEnum, null=False)
    description = fields.CharField(max_length=2000, null=True)
    message = fields.CharField(max_length=2000, null=True)
    status = fields.CharEnumField(enum_type=StatusEnum, null=True)
    type = fields.ForeignKeyField(
        'models_type.Type',
        related_name='problems',
        on_delete=fields.SET_NULL,
        null=True
    )
    time = fields.DateField(null=False)

    class Meta:
        table = "problems"
        app = "models_problems"


class Person(Model):
    class ChannelEnum(str, Enum):
        TG = "TG"
        MAIL = "MAIL"

    id = fields.IntField(null=False, pk=True, unique=True)
    description = fields.CharField(max_length=2000, null=False)
    role = fields.CharField(max_length=2000, null=True)
    full_name = fields.CharField(max_length=2000, null=True)
    login = fields.CharField(max_length=2000, null=True)
    password = fields.CharField(max_length=2000, null=True)
    channel = fields.CharEnumField(enum_type=ChannelEnum, null=False)
    type = fields.CharField(max_length=2000, null=False)

    class Meta:
        table = "person"
        app = "models_person"


class Type(Model):
    id = fields.IntField(null=False, pk=True, unique=True)
    full_name = fields.CharField(null=False, max_length=255)

    class Meta:
        table = "type"
        app = "models_type"
