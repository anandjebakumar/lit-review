from tortoise import fields, models


class Paper(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    authors = fields.CharField(max_length=255)