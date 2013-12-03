from django.db import models

class User(models.Model):
  name = models.TextField(max_length=255)
  password = models.TextField(max_length=255)

  class Meta:
    app_label = 'caca_ao_tesouro'

