from django.contrib import admin
from .models import BuildRelease 
# Register your models here.



@admin.register(BuildRelease)
class BuildRelease_Admin(admin.ModelAdmin) : 
    list_display = ('title' , 'active' , 'open' , 'Release_date' )
