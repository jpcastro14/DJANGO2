# Generated by Django 5.0.7 on 2024-07-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Evid',
            field=models.IntegerField(null=True),
        ),
    ]