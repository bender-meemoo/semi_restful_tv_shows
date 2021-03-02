from django.db import models

# Create your models here.

class TVshowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['addtitle']) < 2:
            errors['addtitle'] = 'Title should at least me 2 characters.'
        if len(postData['addnetwork']) < 3:
            errors['addnetwork'] = 'Network should at least be 3 characters.'
        if len(postData['adddescription']) < 10:
            errors['description'] = 'Description should at least be 10 characters.'
        return errors

class TVshowsManagerEdit(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['edittitle']) < 2:
            errors['edittitle'] = 'Title should at least me 2 characters.'
        if len(postData['editnetwork']) < 3:
            errors['editnetwork'] = 'Network should at least be 3 characters.'
        if len(postData['editdescription']) < 10:
            errors['editdescription'] = 'Description should at least be 10 characters.'
        return errors

class TVshows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=30)
    releaseDate = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    objects = TVshowsManager()
    objects = TVshowsManagerEdit()