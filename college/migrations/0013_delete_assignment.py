# Generated by Django 3.2.9 on 2022-01-12 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0012_remove_teacher_suid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]
