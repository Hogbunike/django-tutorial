# Generated by Django 3.2.19 on 2023-07-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20230709_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
