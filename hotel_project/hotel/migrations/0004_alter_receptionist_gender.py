# Generated by Django 4.0.3 on 2022-04-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_rename_lastname_receptionist_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptionist',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=8),
        ),
    ]
