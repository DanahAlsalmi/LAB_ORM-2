# Generated by Django 4.2.7 on 2023-11-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
