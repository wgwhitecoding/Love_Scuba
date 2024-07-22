# Generated by Django 5.0.7 on 2024-07-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiveLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('best_season', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='travel_images/')),
            ],
        ),
    ]
