# Generated by Django 3.0.5 on 2020-07-12 13:21

from django.db import migrations, models
import notes.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200709_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=notes.models.content_file_name),
        ),
    ]
