from django.contrib import admin
from .models import TestCase
# Register your models here.


@admin.register(TestCase)
class TestCase_Admin(admin.ModelAdmin) : 
    list_display = ('project_name' , 'testsuite_name' , 'title' , 'status' , 'importance' , 'estimate_exec' )
