# Generated by Django 3.2.25 on 2024-05-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0008_bit_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='status',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
