# Generated by Django 4.2.4 on 2023-12-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_customuser_status_alter_outletstaff_status'),
        ('firstpos', '0004_remove_productlist_outlet'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesreceipt',
            name='attending_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.outletstaff'),
        ),
    ]
