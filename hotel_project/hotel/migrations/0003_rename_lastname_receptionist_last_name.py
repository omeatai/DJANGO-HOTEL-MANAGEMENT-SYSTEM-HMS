# Generated by Django 4.0.3 on 2022-04-04 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_paymenttype_receptionist_user_alter_room_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receptionist',
            old_name='lastname',
            new_name='last_name',
        ),
    ]