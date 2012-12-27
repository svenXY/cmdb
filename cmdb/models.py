from django.db import models
from django.forms import ModelForm

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
    name     = models.CharField(u'Name', max_length=40)
    supplier = models.CharField(u'Lieferant', max_length=40)
    status   = models.CharField(max_length=40)
    comment  = models.CharField(u'Kommentar', max_length=200)
    is_template = models.BooleanField(u'Produkt?')
    create_date = models.DateTimeField(u'CI angelegt am')

    def __unicode__(self):
        return self.name
    
    class Meta:
      abstract = True

class CiHardware(CiBase):
    model   = models.ForeignKey('self', limit_choices_to={'is_template':True }, blank=True, null=True, verbose_name="Produkt")
    dimensions  = models.CharField(u'Abmessung', max_length=40)
    usage       = models.CharField(u'Zweck', max_length=80)

    class Meta:
        verbose_name = u'Hardware CI'
        verbose_name_plural = u'Hardware CIs'

class CiHardwareForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CiHardwareForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['model'].widget.attrs['disabled'] = 'disabled'
            self.fields['type'].widget.attrs['disabled'] = 'disabled'
            self.fields['is_template'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = CiHardware

