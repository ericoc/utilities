# Generated by Django 5.1.4 on 2024-12-19 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricusage',
            options={'managed': True, 'ordering': ('hour',), 'verbose_name': 'hour', 'verbose_name_plural': 'hours'},
        ),
    ]