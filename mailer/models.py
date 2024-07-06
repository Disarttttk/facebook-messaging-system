from django.db import models


class Account(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    access_token = models.CharField(max_length=255)
    page_id = models.CharField(max_length=50)  # ID страницы


class Contact(models.Model):
    name = models.CharField(max_length=255)
    facebook_id = models.CharField(max_length=255, unique=True)


class Message(models.Model):
    content = models.TextField()
    send_time = models.DateTimeField()
    delay = models.IntegerField(default=0)
