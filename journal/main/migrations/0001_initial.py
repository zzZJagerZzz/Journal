# Generated by Django 4.0 on 2021-12-20 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_matanaliz', models.CharField(max_length=30)),
                ('status_informatics', models.CharField(max_length=30)),
                ('status_russian', models.CharField(max_length=30)),
                ('status_gymnastic', models.CharField(max_length=30)),
                ('status_yap', models.CharField(max_length=30)),
                ('status_proglang', models.CharField(max_length=30)),
                ('status_inyaz', models.CharField(max_length=30)),
                ('status_oib', models.CharField(max_length=30)),
                ('status_linal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_lastname', models.CharField(max_length=30)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.status')),
            ],
        ),
    ]