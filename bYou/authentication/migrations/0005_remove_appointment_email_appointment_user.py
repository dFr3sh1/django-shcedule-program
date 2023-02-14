# Generated by Django 4.1.6 on 2023-02-14 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_appointment_email_appointment_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]