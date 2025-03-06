# Generated by Django 5.1.6 on 2025-03-06 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_alter_comment_options_alter_commission_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='commissions.commission'),
        ),
    ]
