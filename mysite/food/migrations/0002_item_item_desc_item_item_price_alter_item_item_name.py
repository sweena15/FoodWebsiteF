# Generated by Django 5.0.1 on 2024-01-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='lorem', max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=50),
        ),
    ]
