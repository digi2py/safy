# Generated by Django 3.1.7 on 2021-03-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210302_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
