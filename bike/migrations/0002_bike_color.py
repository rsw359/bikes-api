# Generated by Django 4.0.4 on 2022-05-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='color',
            field=models.CharField(default='red', max_length=100),
            preserve_default=False,
        ),
    ]
