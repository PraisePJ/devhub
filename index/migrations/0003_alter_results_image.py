# Generated by Django 4.1.4 on 2023-03-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_results_ui_remove_results_ux_results_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='image',
            field=models.ImageField(upload_to='results'),
        ),
    ]
