# Generated by Django 5.0.2 on 2024-02-12 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_alter_outletstaff_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlets',
            name='staff',
        ),
    ]
