from nautilus_trader.config import BacktestVenueConfig
from typing import Optional
from nautilus_trader.core.message import Event
from nautilus_trader.indicators.macd import MovingAverageConvergenceDivergence
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.enums import PriceType
from nautilus_trader.model.enums import PositionSide
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.events import PositionOpened
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.objects import Quantity
from nautilus_trader.model.position import Position
from nautilus_trader.trading.strategy import Strategy, StrategyConfig
from nautilus_trader.config import BacktestDataConfig
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.config import BacktestEngineConfig
from nautilus_trader.config import ImportableStrategyConfig
from nautilus_trader.config import LoggingConfig


class VWAPConfig(StrategyConfig):
    InstrumentId: str
    fast_period: int = 12
    slow_period: int = 26
    trad_size: int = 100
    entry_threshold: float = 0.0001

class VWAPStrategy(Strategy):
    def __init__():
        pass
    def on_start():
        pass
    def on_stop():
        pass
    def on_quote_tick():
        pass
    def on_event():
        pass


     



venue = BacktestVenueConfig(
    name="BINANCE",
    oms_type="NETTING",
    account_type="CASH",
    base_currency="USD",
    starting_balance=["10_000 USD"]    

)

engine = BacktestEngineConfig(
    str
)

instruments = catalog.intrsuments()
