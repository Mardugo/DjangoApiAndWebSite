# Generated by Django 4.2.14 on 2024-07-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('givenName', models.CharField(max_length=100)),
                ('firstFamilyName', models.CharField(max_length=100)),
                ('secondFamilyName', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('accountName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
