# Generated by Django 4.1.7 on 2023-08-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=50),
        ),
    ]
