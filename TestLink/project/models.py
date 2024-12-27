from django.db import models
from ckeditor.fields import RichTextField
from django_jalali.db import models as jmodels 
from django.utils import timezone 
# Create your models here.

class ProjectInformation(models.Model) : 
    name         = models.CharField(verbose_name='نام پروژه' , max_length=100 ) 
    description  = RichTextField(verbose_name='توضیحات پروژه' , null = True , blank = True )
    prefix       = models.CharField(verbose_name='اسم ثابت قبل' , max_length=15 , help_text='Like : pro-olt , vlan , ..') 
    requirements = models.BooleanField(verbose_name='آیا پیش نیاز هایی دارد؟' , default=False )
    Testing_Priority = models.BooleanField(verbose_name='آیا اولویت بندی دارد؟' , default=False ) 
    Test_Automation  = models.BooleanField(verbose_name='آیا نیاز به تست اتوماسیون دارد؟' , default=False ) 
    Inventory        = models.BooleanField(verbose_name='آیا انبار دارد؟' , default=False )
    public           = models.BooleanField(verbose_name='آیا به همه نمایش داده شود؟' , default=True )
    Active           = models.BooleanField(verbose_name='آیا پروژه فعال است؟',default=True ) 
    time_create_pro  = jmodels.jDateTimeField(verbose_name='زمان ساخت پروژه' , default=timezone.now )
    update_time      = jmodels.jDateTimeField(verbose_name='زمان به روز رسانی پروژه' , auto_now_add=True )  
    git_project  = models.CharField(verbose_name='لینک پروژه در گیت' , max_length=200  , null = True , blank = True ) 

    def __str__(self) : 
        return f'{self.name}'
    

    class Meta :
        db_table = 'Project'
        verbose_name_plural = 'پروژه ها '



