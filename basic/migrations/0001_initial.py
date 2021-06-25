# Generated by Django 3.2.4 on 2021-06-25 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Paitent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=1000, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.category')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('inactive', 'inactive'), ('active', 'active'), ('finished', 'finished')], max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('due', models.DateField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.doctor')),
                ('pai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
    ]
