from django.db import models

class ExampleObject(models.Model):
    name = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s | %s' % ( self.name, self.pic )

