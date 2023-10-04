# Generated by Django 4.2.2 on 2023-08-30 13:25

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
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_titile', models.CharField(max_length=255)),
                ('complain_message', models.TextField()),
                ('complain_image', models.ImageField(null=True, upload_to='Images')),
                ('to_complain', models.CharField(choices=[('drinking-water', 'Drinking Water'), ('electriciry', 'Electricity'), ('telecommunication', 'Telecommunication')], max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_complains', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]