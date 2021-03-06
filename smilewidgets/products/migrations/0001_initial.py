# Generated by Django 2.0.7 on 2019-12-04 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField(help_text='Value of gift card in cents')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Customer facing name of product', max_length=25)),
                ('code', models.CharField(help_text='Internal facing reference to product', max_length=10)),
                ('price', models.PositiveIntegerField(help_text='Price of product in cents')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Customer facing name of product', max_length=25)),
                ('price', models.PositiveIntegerField(help_text='Price of product in cents')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
