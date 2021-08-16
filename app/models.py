from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Portifolio(TimeStampedModel):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to="portifolio/%Y/%m/%d", blank=False)

    objects = models.Manager()
    class Meta:
        ordering = ("name",)
    
    def __str__(self):
        return self.name

class Projetos(TimeStampedModel):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to="projetos/%Y/%m/%d", blank=False)

    objects = models.Manager()
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Projetos"
    
    def __str__(self):
        return self.name