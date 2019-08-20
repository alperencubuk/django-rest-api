from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length=100)
    street = models.TextField()

    class Meta:
        db_table = 'myuser'
