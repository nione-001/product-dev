# Generated by Django 4.1.3 on 2022-11-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
