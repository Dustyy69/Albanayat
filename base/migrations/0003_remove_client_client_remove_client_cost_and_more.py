# Generated by Django 5.0 on 2024-03-28 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_clients_client_rename_projects_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cost',
        ),
    ]
