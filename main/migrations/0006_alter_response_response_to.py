# Generated by Django 4.2.2 on 2023-10-08 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_response_response_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response_to',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='main.complain'),
        ),
    ]