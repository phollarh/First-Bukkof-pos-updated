# Generated by Django 4.2.4 on 2023-11-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_outlets_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlets',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
