# Generated by Django 3.1.2 on 2020-10-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20201004_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tel_number',
            field=models.CharField(max_length=10),
        ),
    ]