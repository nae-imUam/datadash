# Generated by Django 4.0.4 on 2023-04-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='impact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='insight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='intensity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='likelihood',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='pestle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='relevance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='topic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
