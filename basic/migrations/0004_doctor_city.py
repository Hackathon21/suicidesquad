# Generated by Django 3.2.4 on 2021-06-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(blank=True, choices=[('Ghaziabad', 'Ghaziabad'), ('New Delhi', 'New Delhi'), ('Gurgaon', 'Gurgaon')], max_length=100, null=True),
        ),
    ]
