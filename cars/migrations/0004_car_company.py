# Generated by Django 5.0.5 on 2024-05-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='company',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]