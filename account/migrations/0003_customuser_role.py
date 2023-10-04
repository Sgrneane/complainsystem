# Generated by Django 4.2.2 on 2023-08-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'SUPERADMIN'), (2, 'ADMIN'), (3, 'USER')], default=3, null=True),
        ),
    ]