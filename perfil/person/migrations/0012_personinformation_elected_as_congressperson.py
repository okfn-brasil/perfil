# Generated by Django 2.1 on 2018-08-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_auto_20180817_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinformation',
            name='elected_as_congressperson',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]