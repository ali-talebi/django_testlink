from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class UploadDocument(models.Model) : 
    name = models.CharField(verbose_name='نام داکیومنت' , max_length=100 )
    file = models.FileField(verbose_name='سند ارسال شده' )

    def __str__(self) : 
        return self.name 
    

    class Meta : 
        db_table = 'UploadDocument'
        verbose_name_plural = 'سند های ارسال شده' 

        
