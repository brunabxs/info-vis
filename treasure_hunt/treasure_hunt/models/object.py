from django.db import models

class Object(models.Model):
    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()


    def serialize(self):
        data = {}
        data['uid'] = self.uid
        data['name'] = self.name
        data['description'] = self.description

        return data

    def __str__(self):
        return u"[uid]{0} [name]{1}"
    
    class Meta:
        app_label = "treasure_hunt"
