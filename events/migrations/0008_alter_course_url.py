# Generated by Django 5.0.7 on 2024-09-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_course_options_alter_rating_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
