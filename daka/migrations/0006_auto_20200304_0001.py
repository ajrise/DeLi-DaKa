# Generated by Django 3.0.3 on 2020-03-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daka', '0005_auto_20200303_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='uuid',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]