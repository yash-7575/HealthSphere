# Generated by Django 3.1.7 on 2025-02-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
