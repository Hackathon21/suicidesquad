# Generated by Django 3.2.4 on 2021-06-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20210626_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='medsslip',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
