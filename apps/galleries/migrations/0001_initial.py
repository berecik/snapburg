# Generated by Django 3.0.3 on 2020-03-18 22:20

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnapGallery',
            fields=[
                ('code', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False)),
            ],
            bases=(models.Model, common.models.CreatedMixin),
        ),
    ]
