from django.db import models

class ObjectTip(models.Model):
    text = models.TextField()
    related_object = models.ForeignKey("Object")
    
    # EASY, MEDIUM or HARD (Each object sould have at least one tip of each difficulty level)
    difficulty_level = models.CharField(max_length=255)

    def serialize(self):
        data = {}

        data['text'] = self.text
        return data
    
    def __str__(self):
        return u"[text]{0} [related obj]{1}".format(self.text, self.related_object.name)
    
    class Meta:
        app_label = "treasure_hunt"

