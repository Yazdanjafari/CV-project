# Generated by Django 5.0.6 on 2024-06-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0005_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=255)),
            ],
        ),
    ]