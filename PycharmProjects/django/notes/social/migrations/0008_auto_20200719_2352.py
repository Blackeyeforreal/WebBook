# Generated by Django 3.0.5 on 2020-07-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_posts_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='uploaded_at',
            field=models.DateTimeField(default=20200715),
        ),
    ]