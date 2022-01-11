from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    
    def _str_(self):
        return f'{self.name}'
    
class Participants(models.Model):
    email=models.EmailField(unique=True)
    
    
    def _str_(self):
        return self.email
    
    
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email=models.EmailField()
    date=models.DateField()
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    participants=models.ManyToManyField(Participants,blank=True,null=True)
    
    
    def _str_(self):
        return f'{self.title} - {self.slug}'
    
    
