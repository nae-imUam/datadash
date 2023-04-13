# Generated by Django 4.0.4 on 2023-04-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_data_added_alter_data_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='relevance',
        ),
        migrations.AlterField(
            model_name='data',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='intensity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='likelihood',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.IntegerField(null=True),
        ),
    ]