from django.db import models

# Create your models here.


class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True;


class Course(Base):
    title = models.CharField(max_length=255, blank = False)
    url = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']

    def __str__(self):
        return self.title

class Rating(Base):
    course = models.ForeignKey(Course, related_name='ratings', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = "Ratings"
        unique_together = ['email','course']
        ordering = ['id']



    def __str__(self):
        return f'{self.name} avaliou o curso {self.course} com nota {self.rating}'


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    prepareTime = models.CharField(max_length=50)
    dificulty = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50)
    prepareSteps = models.CharField(max_length=50)
    isVegan = models.BooleanField()

    class Meta: 
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return self.name






