# Generated by Django 4.2.4 on 2023-12-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_outletstaff_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outletstaff',
            name='unique_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
    ]
