# Generated by Django 2.1 on 2018-11-18 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microservices', '0006_auto_20181118_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
