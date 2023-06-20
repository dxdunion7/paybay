# Generated by Django 4.1.3 on 2022-12-02 09:32

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account', models.IntegerField()),
                ('swift', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_address', models.CharField(max_length=50)),
                ('bank_state', models.CharField(max_length=50)),
                ('bank_zip_code', models.CharField(max_length=50)),
                ('bank_country', models.CharField(max_length=50)),
                ('additional_instructions', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Client Withdrawal Bank Details',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('expected_return', models.DecimalField(decimal_places=2, max_digits=50)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
            options={
                'verbose_name_plural': 'Investment Stages',
            },
        ),
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_name', models.CharField(max_length=50)),
                ('wallet_address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'My crypto Wallet addresses',
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_value', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dashboards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Dashboard',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('date', models.DateField(default=core.models.return_date_time)),
            ],
            options={
                'verbose_name_plural': 'Not Needed',
            },
        ),
        migrations.CreateModel(
            name='Tenor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('days', models.CharField(max_length=50)),
                ('percentage', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Investment Tenor',
            },
        ),
        migrations.CreateModel(
            name='WithdrawBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account', models.IntegerField()),
                ('swift', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_address', models.CharField(max_length=50)),
                ('bank_state', models.CharField(max_length=50)),
                ('bank_zip_code', models.CharField(max_length=50)),
                ('bank_country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'My Bank Details',
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('swift', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_address', models.CharField(max_length=50)),
                ('bank_state', models.CharField(max_length=50)),
                ('bank_zip_code', models.CharField(max_length=50)),
                ('bank_country', models.CharField(max_length=50)),
                ('additional_instructions', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Sent', 'Sent')], default='Pending', max_length=9)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard', to='core.dashboard')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Client Withdrawal Details',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depositbank', to='core.withdrawbank')),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cryptos', to='core.crypto')),
            ],
            options={
                'verbose_name_plural': 'Deposit Bank and Crypto Details',
            },
        ),
    ]
