# Generated by Django 5.1.3 on 2024-11-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_details_email_remove_details_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='details',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AddField(
            model_name='details',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=128),
        ),
    ]
