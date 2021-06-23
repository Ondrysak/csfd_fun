# Generated by Django 3.2.4 on 2021-06-23 23:27

import catalog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210623_2301'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='actor',
            name='actors_gin_trgm_idx',
        ),
        migrations.RemoveIndex(
            model_name='movie',
            name='movies_gin_trgm_idx',
        ),
        migrations.AddIndex(
            model_name='actor',
            index=catalog.models.UpperGinIndex(fields=['name'], name='actors_gin_trgm_idx', opclasses=('gin_trgm_ops',)),
        ),
        migrations.AddIndex(
            model_name='movie',
            index=catalog.models.UpperGinIndex(fields=['title'], name='movies_gin_trgm_idx', opclasses=('gin_trgm_ops',)),
        ),
    ]
