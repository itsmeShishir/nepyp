# Generated by Django 5.0.1 on 2024-01-30 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_contactus_created_at_contactus_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoryblog'),
        ),
    ]