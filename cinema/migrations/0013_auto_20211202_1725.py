# Generated by Django 3.1.5 on 2021-12-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0012_screening_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='films',
            name='genre',
            field=models.ManyToManyField(related_name='gnr', to='cinema.Genres'),
        ),
    ]