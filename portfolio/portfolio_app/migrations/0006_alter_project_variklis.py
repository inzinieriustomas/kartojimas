# Generated by Django 4.2.3 on 2023-07-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_rename_engine_project_galia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Variklis',
            field=models.CharField(blank=True, choices=[('3.5', '3.5')], max_length=20),
        ),
    ]
