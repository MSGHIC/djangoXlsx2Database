from django.db import models

# Create your models here.
class UploadForm(models.Model):  
    Title = models.CharField("Enter title", max_length=50)  
    Note  = models.CharField("Enter notes", max_length = 50)  
    date     = models.DateTimeField(auto_now_add=True)
    file      = models.FileField(upload_to = 'uploads/') # for creating file input  
   
    class Meta:  
        db_table = "hubenergy_upload_log"