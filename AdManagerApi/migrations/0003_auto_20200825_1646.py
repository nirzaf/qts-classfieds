# Generated by Django 3.1 on 2020-08-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdManagerApi', '0002_auto_20200825_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion_ad_details',
            name='pa_ad_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]