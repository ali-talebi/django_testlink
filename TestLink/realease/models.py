from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone 
from django_jalali.db import models as jmodels 
# Create your models here.


class BuildRelease(models.Model) : 
    title = models.CharField(verbose_name='نام' , max_length=100 ) 
    description  = RichTextField(verbose_name = 'توضیحات'  , null = True  , blank = True ) 
    active       = models.BooleanField(verbose_name='آیا فعال است ؟' , default=True ) 
    open         = models.BooleanField(verbose_name='آیا باز است این نسخه؟' , default=True ) 
    Release_date = jmodels.jDateTimeField(verbose_name = 'زمان انتشار نسخه' , default = timezone.now ) 
    commit_id    = models.CharField(max_length=1000 , verbose_name='شماره نسخه کامیت' , null = True , blank = True  )
    branch_name  = models.CharField(max_length=1000 , verbose_name='نام برنچ' , null = True , blank = True   )
    release_condition = models.CharField(max_length=1000 , verbose_name='شرایط انتشار'  , null = True , blank = True ) 

    def __str__(self) : 
        return self.title 

    class Meta : 
        db_table = 'BuildRelease'
        verbose_name_plural = 'نسخه های منتشر شده' 
