# Generated by Django 5.0.1 on 2024-01-22 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('posted', 'ارسال شده'), ('failed_supervisor', 'رد شده توسط سرپرست'), ('accepted_supervisor', 'تایید شده توسط سرپرست'), ('failed_manager', 'رد شده توسط مدیر'), ('accepted_manager', 'تایید شده توسط مدیر')], default='posted', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work_flow.requests')),
            ],
        ),
    ]