# Generated by Django 3.2.9 on 2022-01-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0013_delete_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sfile',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='submission',
        ),
    ]
