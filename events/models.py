from django.db import models

# Create your models here.

class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Roles(models.Model):
    Rname = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Categoria"
    
    def __str__(self):
        return self.Rname


class Material(models.Model):
    Mevent = models.ForeignKey(Event, related_name="Material", on_delete=models.CASCADE)
    Mrole = models.ForeignKey(Roles, related_name="Tipo", on_delete=models.CASCADE)
    Mname = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Material"

    def __str__(self):
        return (self.Mname)

class Techcrew(models.Model):
    Tname = models.CharField(max_length=255)
    Trole = models.ForeignKey(Roles, related_name="papel", on_delete=models.CASCADE )

    class Meta:
        verbose_name = "techcrew"
    
    def __str__(self):
        return self.Tname

class Event(Base):
    Evname = models.CharField(max_length=255)
    Evdate = models.DateField()
    Evleader = models.ForeignKey(Techcrew, related_name='techs', on_delete=models.CASCADE)
    Evlocation = models.CharField(max_length=255)
    Evmaterial = models.ForeignKey(Material, related_name="material", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.Evname
    







