# Generated by Django 4.1.4 on 2023-03-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_courses_course_name_courses_course_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='checkbox',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
