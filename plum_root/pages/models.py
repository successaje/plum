from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length = 60)
    permalink = models.CharField(max_length = 60, unique = True)
    update_date = models.DateField('Last Updated')
    bodytext = models.TextField('Page Content', blank = True)

    def __str__(self):
        return str(self.title)