from django.db import models

# Create your models here.

class CiBase(models.Model):
    type     = models.CharField(max_length=30)
    name     = models.CharField(max_length=40)
    supplier = models.CharField(max_length=40)
    status   = models.CharField(max_length=40)
    comment  = models.CharField(max_length=200)
    is_template = models.BooleanField()
    create_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name
    
    class Meta:
      abstract = True

class CiHardware(CiBase):
    model   = models.ForeignKey('self')
    dimensions  = models.CharField(max_length=40)
    usage       = models.CharField(max_length=80)

#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice = models.CharField(max_length=200)
#    votes = models.IntegerField()
