# Generated by Django 4.2.3 on 2023-07-26 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(max_length=100, verbose_name='توضیحات')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
        ),
    ]
