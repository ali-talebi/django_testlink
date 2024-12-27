from django.db import models
from testsuite.models import TestSpecification 
from project.models import ProjectInformation
from ckeditor.fields import RichTextField
# Create your models here.



class TestCase(models.Model) :

    Importance_Level = (
        ('High','High'    ) , 
        ('Medium','Medium') , 
        ('Low','Low'      ) ,  
    )

    STATUS_TEST_CASE = (
        ('Draft','Draft') , 
        ('Ready For Review','Ready For Review') , 
        ('Riveiw in Progress','Riveiw in Progress') , 
        ('Rework' , 'Rework')   , 
        ('Obsolete','Obsolete') , 
        ('Future' , 'Future' )  , 
        ('Final' , 'Final'   )  ,   

    )
    project_name   = models.ForeignKey(ProjectInformation,on_delete=models.CASCADE  , verbose_name='نام پروژه')
    testsuite_name = models.ForeignKey(TestSpecification,on_delete=models.CASCADE , verbose_name='نام دسته بندی تست کیس' )
    title = models.CharField(max_length=100 , verbose_name='نام تست کیس' )
    preconditions  = RichTextField(verbose_name = 'پیش شرایط' , null = True , blank = True ) 
    summary        = RichTextField(verbose_name = 'خلاصه' , null = True , blank = True ) 
    status         = models.CharField(max_length=50 , choices=STATUS_TEST_CASE , default='Draft' ) 
    importance     = models.CharField(max_length=50 , choices=Importance_Level , default='Medium')
    estimate_exec  = models.PositiveSmallIntegerField(verbose_name='زمان اجرا بر حسب دقیقه'  )
    

    def __str__(self ) : 
        return self.title 


    class Meta : 
        db_table = 'TestCase'
        verbose_name_plural = 'تست کیس ها' 