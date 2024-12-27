from django.contrib import admin
from .models import ProjectInformation 
# Register your models here.
@admin.register(ProjectInformation)
class ProjectInformation_Admin(admin.ModelAdmin) : 
    list_display  = ['name' , 'prefix' , 'time_create_pro' , 'public' , 'Active'  ] 
    #list_editable = ['public' , 'active']
