# Generated by Django 3.2 on 2021-05-01 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created', '-email'), 'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
    ]
