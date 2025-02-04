# Generated by Django 4.1.2 on 2022-10-29 05:58

import django.core.serializers.json
import django.db.models.deletion
from django.db import migrations, models

import quant_candles.models.candles
import quant_candles.models.trades


def fake(*args):
    return


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="GlobalSymbol",
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
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="name"),
                ),
                (
                    "notional",
                    models.DecimalField(
                        blank=True,
                        decimal_places=38,
                        max_digits=76,
                        null=True,
                        verbose_name="notional",
                    ),
                ),
            ],
            options={
                "verbose_name": "global symbol",
                "verbose_name_plural": "global symbols",
                "db_table": "quant_candles_global_symbol",
            },
        ),
        migrations.CreateModel(
            name="Symbol",
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
                    "exchange",
                    models.CharField(
                        choices=[
                            ("binance", "Binance"),
                            ("bitfinex", "Bitfinex"),
                            ("bitmex", "BitMEX"),
                            ("bybit", "Bybit"),
                            ("coinbase", "Coinbase"),
                        ],
                        max_length=255,
                        verbose_name="exchange",
                    ),
                ),
                (
                    "api_symbol",
                    models.CharField(max_length=255, verbose_name="API symbol"),
                ),
                (
                    "significant_trade_filter",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="If trades are aggregated, they can be further filtered according to the algorithm described in the documentation.",
                        verbose_name="significant trade filter",
                    ),
                ),
                (
                    "global_symbol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="symbols",
                        to="quant_candles.globalsymbol",
                    ),
                ),
                (
                    "should_aggregate_trades",
                    models.BooleanField(
                        default=False,
                        help_text="Should trades be aggregated?",
                        verbose_name="aggregate trades",
                    ),
                ),
                (
                    "symbol_type",
                    models.CharField(
                        choices=[
                            ("spot", "spot"),
                            ("perp", "perp"),
                            ("future", "future"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
            ],
            options={
                "verbose_name": "symbol",
                "verbose_name_plural": "symbols",
                "db_table": "quant_candles_symbol",
                "ordering": ("exchange", "api_symbol"),
                "unique_together": {
                    (
                        "exchange",
                        "api_symbol",
                        "should_aggregate_trades",
                        "significant_trade_filter",
                    )
                },
            },
        ),
        migrations.CreateModel(
            name="Candle",
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
                    "code_name",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="code name"
                    ),
                ),
                ("date_from", models.DateField(null=True, verbose_name="date from")),
                ("date_to", models.DateField(null=True, verbose_name="date to")),
                (
                    "json_data",
                    models.JSONField(
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                        verbose_name="json data",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "symbols",
                    models.ManyToManyField(
                        db_table="quant_candles_candle_symbol",
                        to="quant_candles.symbol",
                        verbose_name="symbols",
                    ),
                ),
            ],
            options={
                "verbose_name": "candle",
                "verbose_name_plural": "candles",
                "db_table": "quant_candles_candle",
            },
        ),
        migrations.CreateModel(
            name="CandleData",
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
                        verbose_name="frequency",
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
                    "file_data",
                    models.FileField(
                        blank=True,
                        upload_to=fake,
                        verbose_name="file data",
                    ),
                ),
                (
                    "json_cache",
                    models.JSONField(
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                        verbose_name="json cache",
                    ),
                ),
                (
                    "file_cache",
                    models.FileField(
                        blank=True,
                        upload_to=fake,
                        verbose_name="file cache",
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
                "verbose_name": "candle data",
                "verbose_name_plural": "candle data",
                "db_table": "quant_candles_candle_data",
                "ordering": ("timestamp",),
            },
        ),
        migrations.CreateModel(
            name="TradeData",
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
                    "uid",
                    models.CharField(blank=True, max_length=255, verbose_name="uid"),
                ),
                (
                    "file_data",
                    models.FileField(
                        blank=True,
                        upload_to=quant_candles.models.trades.upload_trade_data_to,
                        verbose_name="file data",
                    ),
                ),
                (
                    "ok",
                    models.BooleanField(
                        db_index=True, default=False, null=True, verbose_name="ok"
                    ),
                ),
                (
                    "symbol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="aggregated",
                        to="quant_candles.symbol",
                    ),
                ),
                (
                    "frequency",
                    models.PositiveIntegerField(
                        choices=[(1, "Minute"), (60, "Hour")],
                        db_index=True,
                        verbose_name="frequency",
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
            ],
            options={
                "verbose_name": "trade data",
                "verbose_name_plural": "trade data",
                "db_table": "quant_candles_trade_data",
                "ordering": ("timestamp",),
            },
        ),
        migrations.CreateModel(
            name="AdaptiveCandle",
            fields=[],
            options={
                "verbose_name": "adaptive candle",
                "verbose_name_plural": "adaptive candles",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("quant_candles.candle",),
        ),
        migrations.CreateModel(
            name="ConstantCandle",
            fields=[],
            options={
                "verbose_name": "constant candle",
                "verbose_name_plural": "constant candles",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("quant_candles.candle",),
        ),
        migrations.CreateModel(
            name="ImbalanceCandle",
            fields=[],
            options={
                "verbose_name": "imbalance candle",
                "verbose_name_plural": "imbalance candles",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("quant_candles.candle",),
        ),
        migrations.CreateModel(
            name="RunCandle",
            fields=[],
            options={
                "verbose_name": "run candle",
                "verbose_name_plural": "run candles",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("quant_candles.candle",),
        ),
    ]
