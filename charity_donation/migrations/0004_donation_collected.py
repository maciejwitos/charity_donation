# Generated by Django 3.0.4 on 2020-03-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='collected',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
