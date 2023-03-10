# Generated by Django 4.1.6 on 2023-02-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('COACH', 'Coach'), ('CUSTOMER', 'Customer'), ('STAFF', 'Staff')], max_length=30, verbose_name='Rôle'),
        ),
    ]
