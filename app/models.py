from django.db import models

# Create your models here.
class Portifolio(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to="portifolio/%Y/%m/%d", blank=False)
    created = models.CharField(max_length=255)
    modified = models.CharField(max_length=255)

    objects = models.Manager()
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Projetos(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to="projetos/%Y/%m/%d", blank=False)
    created = models.CharField(max_length=255)
    modified = models.CharField(max_length=255)

    objects = models.Manager()
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.name