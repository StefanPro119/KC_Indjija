# Generated by Django 3.1.5 on 2021-12-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_remove_screening_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='start_time',
            field=models.DateField(null=True),
        ),
    ]