# Generated by Django 4.2.17 on 2024-12-26 12:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_suite_name', models.CharField(max_length=100, verbose_name='اسم testsuite ')),
                ('Details', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created', django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsuite.testspecification', verbose_name='نسخه تست بالا دستی')),
            ],
            options={
                'verbose_name_plural': 'دسته بندی تست کیس ها  ',
                'db_table': 'TestSpecification',
            },
        ),
    ]