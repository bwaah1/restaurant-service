# Generated by Django 5.0.6 on 2024-05-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_cook_years_of_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterField(
            model_name='cook',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cook',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]