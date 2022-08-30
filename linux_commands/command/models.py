from django.db import models
from category.models import Category

class Command(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Command"
        verbose_name_plural = "Commands"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("command_detail", kwargs={"pk": self.pk})
