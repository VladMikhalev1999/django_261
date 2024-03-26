from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


