from django.db import models

# Create your models here.



class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=800)
    message = models.TextField()
    
    
    def __str__(self):
        return self.fullname
    
    
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        
        
        
        
class NewsLetter(models.Model):
    email = models.EmailField()
    
    
    def __str__(self):
        return self.email
    
        
    
    class Meta:
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetters"
        