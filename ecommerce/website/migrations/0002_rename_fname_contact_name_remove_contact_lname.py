# Generated by Django 4.1.4 on 2023-05-30 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
    ]