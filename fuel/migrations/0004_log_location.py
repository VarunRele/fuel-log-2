# Generated by Django 4.2.17 on 2024-12-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0003_log_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Location of Petrol pump'),
        ),
    ]
