# Generated by Django 3.0.5 on 2020-07-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_book_reck'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_reck',
            name='bid',
            field=models.ImageField(default=3, max_length=311, upload_to=''),
        ),
    ]
