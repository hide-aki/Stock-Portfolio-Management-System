# Generated by Django 2.1.5 on 2019-11-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_symbols_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPrediction',
            fields=[
                ('symbol', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('insample', models.TextField()),
                ('outsample', models.TextField()),
                ('result', models.TextField()),
                ('insampleMse', models.FloatField()),
                ('insampleR2', models.FloatField()),
                ('outsampleMse', models.FloatField()),
                ('outsampleR2', models.FloatField()),
            ],
            options={
                'db_table': 'historyPrediction',
            },
        ),
    ]