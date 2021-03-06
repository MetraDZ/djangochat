# Generated by Django 3.1.7 on 2021-04-07 14:58

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=30, null=True, unique=True, validators=[api.validators.validate_email]),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.author'),
        ),
    ]
