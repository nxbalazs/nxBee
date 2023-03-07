# Generated by Django 4.1.6 on 2023-03-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hive_management', '0002_alter_hive_created_on_alter_inspection_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hive',
            name='color',
            field=models.CharField(max_length=50, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='created_on',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='frames',
            field=models.IntegerField(verbose_name='Frames'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Hive Name'),
        ),
        migrations.AlterField(
            model_name='hive',
            name='supers',
            field=models.IntegerField(verbose_name='Supers'),
        ),
    ]
