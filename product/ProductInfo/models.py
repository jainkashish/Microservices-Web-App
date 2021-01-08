from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        db_table: 'product'
