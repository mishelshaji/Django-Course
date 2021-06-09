from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=15,
        unique=True
    )

    description = models.TextField(
        max_length=500
    )

    color = models.CharField(
        max_length=10,
        default='#000000'
    )

    def __str__(self):
        return self.name