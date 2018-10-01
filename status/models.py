from django.conf import settings 
from django.db import models

'''
JSON -- JavaScript Object Notation
'''


def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass
'''
A Manager's base QuerySet returns all object in the system.
You can override a Manager's base QuerySet by overriding the Manager.get_queryset() method.
get_queryset() should return a QuerySet witht he properties you require. 
https://docs.djangoproject.com/ko/2.1/topics/db/managers/
'''
class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.models, using=self.db)


# Create your models here.
class Status(models.Model): #fb status, instagram post, tweet, linkedin post
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(null=True, blank=True)
    image       = models.ImageField(upload_to=upload_status_image, null=True, blank=True) #Django Storage --> AWS S3
    updated     = models.DateTimeField(auto_now = True)
    timestamp   = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.content)[:50] # up to 50 character
    
    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'