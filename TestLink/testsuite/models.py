from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone 
from django_jalali.db import models as jmodels 
# Create your models here.



class TestSpecification(models.Model) : 
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , verbose_name='نسخه تست بالا دستی' , null = True , blank = True ) 
    test_suite_name = models.CharField(verbose_name='اسم testsuite ' , max_length=100 ) 
    Details = RichTextField(verbose_name = 'توضیحات' , null = True , blank = True ) 
    created = jmodels.jDateTimeField(default = timezone.now , verbose_name = 'زمان ایجاد' ) 

    def __str__(self ) : 
        return self.test_suite_name 
    
    class Meta : 
        db_table = 'TestSpecification'
        verbose_name_plural = 'دسته بندی تست کیس ها  '
    


