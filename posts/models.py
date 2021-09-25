from django.db import models


class Post(models.Model):
    text = models.TextField()

    # Display the first 50 characters of the text field
    def __str__(self):
        return self.text[:50]
