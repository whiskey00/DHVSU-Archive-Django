# Generated by Django 4.2 on 2023-10-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
