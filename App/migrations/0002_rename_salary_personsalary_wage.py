# Generated by Django 4.1.2 on 2023-07-11 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personsalary',
            old_name='salary',
            new_name='wage',
        ),
    ]