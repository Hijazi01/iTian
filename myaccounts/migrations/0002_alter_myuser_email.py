# Generated by Django 4.2.1 on 2023-06-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
