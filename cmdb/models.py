from django.db import models

# Create your models here.

class Category(models.Model):

    SUBCAT_HW = 1
    SUBCAT_LD = 2
    SUBCAT_SW = 3
    SUBCATEGORIES = (
        (SUBCAT_HW, u'Hardware'),
        (SUBCAT_LD, u'Logical Device'),
        (SUBCAT_SW, u'Software'),
    )

    name = models.CharField(u'Name', max_length=30)
    slug = models.SlugField(unique=True)
    subcat= models.SmallIntegerField(u'Sub-Kategorien', choices=SUBCATEGORIES, default=SUBCAT_HW)
    description = models.TextField(u'Beschreibung', blank=True)

    class Meta:
        verbose_name = u'Kategorie'
        verbose_name_plural = u'Kategorien'

    def __unicode__(self):
        return self.name

class CiBase(models.Model):
    type     = models.ForeignKey('Category', limit_choices_to = {'subcat': 1})
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
    model   = models.ForeignKey('self', limit_choices_to={'is_template':True }, blank=True, null=True)
    dimensions  = models.CharField(max_length=40)
    usage       = models.CharField(max_length=80)

