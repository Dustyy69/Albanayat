# Generated by Django 5.0 on 2024-04-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_client_client_remove_client_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client_feedback',
        ),
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(null=True, upload_to='base/uploads/projects'),
        ),
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(null=True, upload_to='base/uploads/clients'),
        ),
    ]
