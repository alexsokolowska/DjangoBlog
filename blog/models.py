from django.db import models
from django.utils import timezone

#https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

class Post(models.Model): 
#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
    author = models.ForeignKey('auth.User') #a link to another model, foreign key in a database
    title = models.CharField(max_length=200) #a limited number of characters.
    text = models.TextField() #text without a limit
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # return a human readable string
        return self.title
