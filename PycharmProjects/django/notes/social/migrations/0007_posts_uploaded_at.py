# Generated by Django 3.0.5 on 2020-07-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20200719_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='uploaded_at',
            field=models.DateTimeField(default=4),
        ),
    ]
