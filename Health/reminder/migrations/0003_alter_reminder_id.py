# Generated by Django 5.1.6 on 2025-02-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20250221_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
