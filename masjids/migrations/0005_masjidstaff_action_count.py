# Generated by Django 2.0 on 2020-03-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masjids', '0004_auto_20200302_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='masjidstaff',
            name='action_count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Actions till now'),
        ),
    ]