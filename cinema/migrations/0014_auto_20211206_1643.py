# Generated by Django 3.1.5 on 2021-12-06 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0013_auto_20211202_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='genre_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre_id', to='cinema.genres'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
