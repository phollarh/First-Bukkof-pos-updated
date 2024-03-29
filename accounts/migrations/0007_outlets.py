# Generated by Django 4.1.3 on 2023-11-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_first_name_customuser_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outlets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('outlet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
