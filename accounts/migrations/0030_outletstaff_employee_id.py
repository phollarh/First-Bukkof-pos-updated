# Generated by Django 4.2.4 on 2023-12-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_outletstafflogin_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='outletstaff',
            name='Employee_id',
            field=models.CharField(default='1111', max_length=20),
            preserve_default=False,
        ),
    ]