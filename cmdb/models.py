from django.db import models
from django.forms import ModelForm, HiddenInput

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
    type     = models.ForeignKey(Category, limit_choices_to = {'subcat': 1}, verbose_name=u'Kategorie')
    name     = models.CharField(u'Name', max_length=40, db_index=True,
                                unique=True)
    status   = models.CharField(max_length=40)
    comment  = models.CharField(u'Kommentar', max_length=200, blank=True)
    supplier = models.CharField(u'Lieferant', max_length=40)
    vendor = models.CharField(u'Hersteller', max_length=40, blank=True)
    create_date = models.DateTimeField(u'CI angelegt am', auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
      abstract = True

class CiHardware(CiBase):
    model   = models.ForeignKey('self', limit_choices_to={'model__name':None }, blank=True, null=True, verbose_name="Produkt")
    dimensions  = models.CharField(u'Abmessung', max_length=40)
    usage       = models.CharField(u'Zweck', max_length=80, blank=True)

    class Meta:
        verbose_name = u'Hardware CI'
        verbose_name_plural = u'Hardware CIs'

class PrdHardwareForm(ModelForm):
    class Meta:
        model = CiHardware
        exclude = { 'date_created', }

class CiHardwareForm(ModelForm):
    class Meta:
        model = CiHardware
        exclude = { 'date_created', }
        widgets = { 
            'type' : HiddenInput,
            'model' : HiddenInput,
            'dimensions' : HiddenInput,
            'vendor' : HiddenInput
        }

