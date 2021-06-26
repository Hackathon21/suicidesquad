# Generated by Django 3.2.4 on 2021-06-25 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedsSlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.meds')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
        migrations.CreateModel(
            name='MedsBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('meds', models.ManyToManyField(to='basic.MedsSlip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnoseSlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=False)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.diagnosis')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnoseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('services', models.ManyToManyField(to='basic.DiagnoseSlip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.doctor')),
                ('pai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.paitent')),
            ],
        ),
    ]
