# Generated by Django 5.1.2 on 2024-11-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name='Ваше имя')),
                ('comtent', models.TextField(verbose_name='Собшение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]