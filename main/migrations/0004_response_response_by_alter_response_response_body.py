# Generated by Django 4.2.2 on 2023-10-08 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_complain_options_alter_complain_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='response_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_body',
            field=models.TextField(),
        ),
    ]
