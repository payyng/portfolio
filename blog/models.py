from django.db import models

# Create your models here.
class Blog(models.Model):

    Title = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now_add=False)
    Body = models.TextField()
    Image = models.ImageField(upload_to='images/')

    def __str__ (self):
        return self.Title

    def summary(self):
        return self.Body[:50]

    def pretty_date(self):
        return self.Date.strftime('%b %e')
