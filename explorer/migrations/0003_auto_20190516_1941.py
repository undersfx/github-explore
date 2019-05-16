# Generated by Django 2.2.1 on 2019-05-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_auto_20190516_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='created_at',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='repository',
            name='html_url',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='repository',
            name='login',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_by',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='display_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='released',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='topic',
            name='short_description',
            field=models.CharField(max_length=512),
        ),
    ]