# Generated by Django 4.1.3 on 2023-11-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_outlets_outlet_customuser_outlet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='outlet',
            field=models.ManyToManyField(blank=True, to='accounts.outlets'),
        ),
    ]
