from enum import unique
# from quopri import quote

from tortoise.models import Model
from tortoise import fields


class Problems(Model):
    id = fields.IntField(null=False, pk=True, unique=True)
    description = fields.CharField(max_length=2000, null=False)
    message = fields.CharField(max_length=2000, null=False)
    status = fields.CharField(max_length=2000, null=False)
    type = fields.CharField(max_length=2000, null=False)
    time = fields.DateField(max_length=2000, null=False)

    class Meta:
        table = "problems"
        app = "models_problems"


class Person(Model):
    id = fields.IntField(null=False, pk=True, unique=True)
    description = fields.CharField(max_length=2000, null=False)
    role = fields.CharField(max_length=2000, null=False)
    full_name = fields.CharField(max_length=2000, null=False)
    login = fields.CharField(max_length=2000, null=False)
    password = fields.CharField(max_length=2000, null=False)
    channel = fields.CharField(max_length=2000, null=False)
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
