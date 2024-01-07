# Generated by Django 4.2.7 on 2023-12-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(max_length=100, null=True)),
            ],
        ),
    ]
