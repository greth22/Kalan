from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TAG_TYPES = (
             (0,'User'),
             (1,'System'),
             (2,'Admin'),
             )

class Account(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return "%s %s" % (self.name, self.id)
    
class Tag(models.Model):
    text = models.CharField(max_length=60)
    type = models.SmallIntegerField(choices=TAG_TYPES)
    owner = models.ForeignKey(User, blank=True, null=True)
    private = models.BooleanField()
    
    def url(self):
        return self.text        
    
    def __unicode__(self):
        return self.text
    
class Ticket(models.Model):
    subject = models.CharField(max_length=60)
    account = models.ManyToManyField(Account)
    tags    = models.ManyToManyField(Tag)    
    
    def __unicode__(self):
        return self.subject
            
class Entry(models.Model):
    subject = models.CharField(max_length=60)
    ticket = models.ForeignKey(Ticket)
    body = models.TextField()
    
    def __unicode__(self):
        return self.subject

    

    