from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.png')


    def __str__(self):
        return str(self.name)

