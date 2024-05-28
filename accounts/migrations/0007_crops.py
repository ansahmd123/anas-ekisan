# Generated by Django 3.2.25 on 2024-05-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameineng', models.CharField(max_length=100)),
                ('nameinurdu', models.CharField(max_length=100)),
                ('nameinhindi', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='crop_images/')),
            ],
        ),
    ]
