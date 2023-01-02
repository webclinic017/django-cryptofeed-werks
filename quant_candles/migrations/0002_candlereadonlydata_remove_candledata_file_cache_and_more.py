# Generated by Django 4.1.4 on 2023-01-01 00:40

import django.core.serializers.json
import django.db.models.deletion
from django.db import migrations, models

import quant_candles.models.candles


class Migration(migrations.Migration):

    dependencies = [
        ("quant_candles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CandleReadOnlyData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(db_index=True, verbose_name="timestamp"),
                ),
                (
                    "candle_id",
                    models.BigIntegerField(db_index=True, verbose_name="candle"),
                ),
                (
                    "json_data",
                    models.JSONField(
                        default=dict,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        verbose_name="json data",
                    ),
                ),
            ],
            options={
                "verbose_name": "candle data",
                "verbose_name_plural": "candle data",
                "db_table": "quant_candles_candle_read_only_data",
                "ordering": ("timestamp",),
            },
        ),
        migrations.RemoveField(
            model_name="candledata",
            name="file_cache",
        ),
        migrations.RemoveField(
            model_name="candledata",
            name="file_data",
        ),
        migrations.RemoveField(
            model_name="candledata",
            name="frequency",
        ),
        migrations.RemoveField(
            model_name="candledata",
            name="json_cache",
        ),
        migrations.AlterField(
            model_name="candle",
            name="json_data",
            field=models.JSONField(
                default=dict,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                verbose_name="json data",
            ),
        ),
        migrations.AlterField(
            model_name="candle",
            name="symbols",
            field=models.ManyToManyField(
                db_table="quant_candles_candle_symbol",
                to="quant_candles.symbol",
                verbose_name="symbol",
            ),
        ),
        migrations.AlterField(
            model_name="candledata",
            name="candle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quant_candles.candle",
                verbose_name="candle",
            ),
        ),
        migrations.AlterField(
            model_name="candledata",
            name="json_data",
            field=models.JSONField(
                default=dict,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                verbose_name="json data",
            ),
        ),
        migrations.CreateModel(
            name="CandleCache",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(db_index=True, verbose_name="timestamp"),
                ),
                (
                    "frequency",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Minute"),
                            (60, "Hour"),
                            (1440, "Day"),
                            (10080, "Week"),
                        ],
                        db_index=True,
                        verbose_name="frequency",
                    ),
                ),
                (
                    "file_data",
                    models.FileField(
                        blank=True,
                        upload_to=quant_candles.models.candles.upload_data_to,
                        verbose_name="file data",
                    ),
                ),
                (
                    "json_data",
                    models.JSONField(
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                        verbose_name="json data",
                    ),
                ),
                (
                    "candle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data",
                        to="quant_candles.candle",
                    ),
                ),
            ],
            options={
                "verbose_name": "candle cache",
                "verbose_name_plural": "candle cache",
                "db_table": "quant_candles_candle_cache",
                "ordering": ("timestamp",),
            },
        ),
        migrations.CreateModel(
            name="TimeBasedCandle",
            fields=[],
            options={
                "verbose_name": "time based candle",
                "verbose_name_plural": "time based candles",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("quant_candles.candle",),
        ),
    ]
