from django.contrib import admin
from .models import TestSpecification 
# Register your models here.


@admin.register(TestSpecification)
class TestSpecification_Admin(admin.ModelAdmin) : 
    list_display = ('parent' , 'test_suite_name' , 'created' )