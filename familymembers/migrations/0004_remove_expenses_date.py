# Generated by Django 3.1.2 on 2020-11-23 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familymembers', '0003_expenses_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='date',
        ),
    ]