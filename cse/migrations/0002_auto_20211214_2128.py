# Generated by Django 3.2.9 on 2021-12-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='m1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='m2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='m3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='r1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='r2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='r3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]