# Generated by Django 4.2.3 on 2023-07-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_project_utl_alter_project_utl1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='utl',
            new_name='Engine',
        ),
    ]
