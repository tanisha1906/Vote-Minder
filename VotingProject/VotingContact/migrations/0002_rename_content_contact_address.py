# Generated by Django 4.1 on 2024-03-27 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VotingContact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='address',
        ),
    ]