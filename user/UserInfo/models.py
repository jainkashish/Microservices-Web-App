from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    products_liked = models.IntegerField(default=0)


    class Meta:
        db_table: 'user'
