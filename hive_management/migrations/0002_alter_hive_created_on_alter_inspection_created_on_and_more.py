# Generated by Django 4.1.6 on 2023-03-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hive_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hive',
            name='created_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='created_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='created_on',
            field=models.DateField(),
        ),
    ]
