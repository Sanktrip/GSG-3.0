import logging
from data import Data, DataDeque
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[
                        #logging.StreamHandler(),  
                        logging.FileHandler('websocket.log', mode="w") 
                    ])

datastream_10 = DataDeque(10)

def message_handler(_, message):
    datastream_10.process_message(message)

my_client = SpotWebsocketStreamClient(on_message=message_handler, is_combined=True, timeout=10)

my_client.kline(symbol="btcusdt", interval="1m", action=SpotWebsocketStreamClient.ACTION_SUBSCRIBE)

try:
    while True:
        user_input = input("Inputs:\n- p: Print Datastream\n- CTRL-d: Exit Gracefully\n")
        if user_input == 'p':
            print(datastream_10)
    
except EOFError:
    logging.info("Webstream Ending, EOF was entered")
    my_client.stop()

