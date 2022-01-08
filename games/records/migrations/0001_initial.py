# Generated by Django 4.0.1 on 2022-01-08 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winners', models.ManyToManyField(to='records.Player', verbose_name='Players')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_date', models.DateTimeField(verbose_name='Date')),
                ('g_location', models.CharField(default='NA', max_length=100, verbose_name='location')),
                ('g_tag', models.CharField(default='NA', max_length=100, verbose_name='Descriptor')),
                ('g_notes', models.TextField(null=True, verbose_name='Notes')),
                ('g_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.game', verbose_name='Game Name')),
                ('g_players', models.ManyToManyField(to='records.Player', verbose_name='Players')),
                ('g_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='records.result', verbose_name='Winners')),
            ],
        ),
    ]