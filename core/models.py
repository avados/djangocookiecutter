from django.db import models


class Ccm(models.Model):
    field1 = models.TextField(
        max_length=255,
        blank=True,
    )
