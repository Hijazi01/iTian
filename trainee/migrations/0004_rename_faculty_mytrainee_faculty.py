# Generated by Django 4.2.1 on 2023-06-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0003_alter_mytrainee_faculty_alter_mytrainee_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytrainee',
            old_name='Faculty',
            new_name='faculty',
        ),
    ]