# Generated by Django 4.2.3 on 2023-07-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0002_alter_foods_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='امتیاز'),
        ),
    ]
