from quant_candles.exchanges.api import api
from quant_candles.management.base import BaseTradeDataCommand


class Command(BaseTradeDataCommand):
    help = "Get trades from exchange API or S3."

    def handle(self, *args, **options) -> None:
        """Run command."""
        kwargs = super().handle(*args, **options)
        for k in kwargs:
            api(**k)
