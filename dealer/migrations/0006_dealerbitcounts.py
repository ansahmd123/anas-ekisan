# Generated by Django 3.2.25 on 2024-05-20 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20240519_1359'),
        ('dealer', '0005_bit_farmer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerBitCounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_bid_count', models.IntegerField(default=0)),
                ('subscription_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.subscription')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
