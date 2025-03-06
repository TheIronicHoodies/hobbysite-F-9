# Generated by Django 5.1.6 on 2025-03-06 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='entry',
            field=models.TextField(default=-2044),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='wiki.articlecategory'),
        ),
    ]
