# Generated by Django 3.2.3 on 2021-06-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
