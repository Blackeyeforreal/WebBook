# Generated by Django 3.0.5 on 2020-07-14 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_book_reck_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcomment', models.TextField(default=3, max_length=255)),
                ('likes', models.ImageField(default=4, max_length=255, upload_to='')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.posts')),
            ],
        ),
    ]
