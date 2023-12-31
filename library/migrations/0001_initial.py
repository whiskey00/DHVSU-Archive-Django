# Generated by Django 4.2 on 2023-10-04 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=64)),
                ('abbreviation', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=64)),
                ('abbreviation', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('school_year', models.CharField(max_length=9)),
                ('abstract', models.TextField()),
                ('course', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='library.course')),
                ('group', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='library.group')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='library.department'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('course', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='library.course')),
            ],
        ),
    ]
