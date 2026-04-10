from django.db import models
from django.conf import settings
# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1, related_name='documents')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    name_company= models.CharField(max_length=100)
    valid= models.BooleanField(default=False)
    start_date= models.DateField()
    end_date= models.DateField()
    date_of_add = models.DateField(auto_now_add=True)
    data_of_update = models.DateField(auto_now=True)
    
    
    def __str__ (self):
        return self.name_company