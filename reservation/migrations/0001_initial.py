# Generated by Django 4.2.3 on 2023-07-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('email', models.EmailField(max_length=245, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=100, verbose_name='شماره تماس')),
                ('number', models.IntegerField(max_length=50, verbose_name='تعداد')),
                ('date', models.DateTimeField(max_length=100, verbose_name='تاریخ')),
                ('time', models.TextField(max_length=50, verbose_name='ساعت')),
            ],
        ),
    ]
