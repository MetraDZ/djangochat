# Generated by Django 3.1.7 on 2021-04-07 15:24

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210407_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=100, null=True, validators=[api.validators.validate_message]),
        ),
    ]