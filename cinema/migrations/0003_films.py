# Generated by Django 3.1.5 on 2021-12-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lenght_min', models.IntegerField()),
            ],
        ),
    ]