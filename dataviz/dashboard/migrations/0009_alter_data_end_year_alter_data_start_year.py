# Generated by Django 4.0.4 on 2023-04-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_data_end_year_alter_data_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
