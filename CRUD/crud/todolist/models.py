from django.db import models

# Create your models here.


class TODO(models.Model):
    title = models.CharField('Case name', max_length=200)
    taskcomplete = models.BooleanField('Complete', default=False)

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.title
