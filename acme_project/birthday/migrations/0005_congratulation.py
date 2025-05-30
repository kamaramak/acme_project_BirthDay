# Generated by Django 5.1.1 on 2025-05-30 08:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_birthday_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Congratulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поздравдения')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='congratulation', to='birthday.birthday')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
