# Generated by Django 3.1.5 on 2021-12-02 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_films'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=2)),
                ('number', models.IntegerField()),
                ('rooms_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_id', to='cinema.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_id', to='cinema.films')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_id', to='cinema.rooms')),
            ],
        ),
    ]