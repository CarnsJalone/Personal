from django.db import models

class Connector(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} at {} sent you: \n {}'.format(first_name, last_name, email, body)

