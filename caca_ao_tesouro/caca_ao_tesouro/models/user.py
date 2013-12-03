from django.db import models

class User(models.Model):
  name = models.TextField(max_length=255)
  password = models.TextField(max_length=255)

  class Meta:
    app_label = 'caca_ao_tesouro'


  @classmethod
  def validate_user(cls, name, password):
      user = cls.objects.filter(name=name, password=password)

      if user:
        return True
      else:
        return False


  def __str__(self):
    return "{0}:{1}".format(self.name, self.password)
