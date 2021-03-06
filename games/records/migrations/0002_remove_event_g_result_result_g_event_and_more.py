# Generated by Django 4.0.1 on 2022-01-10 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='g_result',
        ),
        migrations.AddField(
            model_name='result',
            name='g_event',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='records.event'),
        ),
        migrations.AlterField(
            model_name='result',
            name='winners',
            field=models.ManyToManyField(to='records.Player', verbose_name='Winners'),
        ),
    ]
