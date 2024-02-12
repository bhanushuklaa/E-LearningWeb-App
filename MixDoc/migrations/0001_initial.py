# Generated by Django 3.2.4 on 2022-04-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]