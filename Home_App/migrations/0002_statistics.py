# Generated by Django 5.0.6 on 2024-06-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Happy_Clients', models.IntegerField()),
                ('Projects', models.IntegerField()),
                ('Job_history_in_years', models.IntegerField()),
                ('Awards', models.IntegerField()),
            ],
        ),
    ]
