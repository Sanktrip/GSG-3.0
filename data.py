import json
from typing import List
from candlestick import Candlestick
import logging
from collections import deque

class Data():
    def __init__(self):
        self.data: List[Candlestick] = []

    def process_message(self, message):
        parse_data = json.loads(message)

        if message[0:3] == "{\"r":
            logging.info("Data Stream Starting")
            return

        try:
            data_obj = parse_data['data']

            kline_obj = data_obj['k']
            
            is_closed = kline_obj['x']
            if not is_closed:
                return
            
            highp = kline_obj['h']
            lowp = kline_obj['l']
            openp = kline_obj['o']
            closep = kline_obj['c']          
            qvolume = kline_obj['q']

            self.data.append(Candlestick(openp, closep, highp, lowp, qvolume))
            
        except json.JSONDecodeError as error:
            print(f"Error decoding JSON: {error}")

    def __str__(self) -> str:
        if len(self.data) == 0:
            return "\n[Empty]\n"
        string = ""
        for candlestick in self.data:
            string += "----------------------------\n"
            string += (candlestick.__str__() + "\n")
        
        return string
        
class DataDeque(Data):
    def __init__(self, size):
        self.data: deque = deque(maxlen=size)

    def process_message(self, message):
        parse_data = json.loads(message)

        if message[0:3] == "{\"r":
            logging.info("Data Stream Starting")
            return

        try:
            data_obj = parse_data['data']

            kline_obj = data_obj['k']
            
            is_closed = kline_obj['x']
            if not is_closed:
                return
            
            highp = kline_obj['h']
            lowp = kline_obj['l']
            openp = kline_obj['o']
            closep = kline_obj['c']          
            qvolume = kline_obj['q']
            

            self.data.append(Candlestick(openp, closep, highp, lowp, qvolume))
            
        except json.JSONDecodeError as error:
            print(f"Error decoding JSON: {error}")
