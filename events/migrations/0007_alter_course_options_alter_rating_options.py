# Generated by Django 5.0.7 on 2024-08-22 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_course_options_alter_rating_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['id'], 'verbose_name': 'Rating', 'verbose_name_plural': 'Ratings'},
        ),
    ]