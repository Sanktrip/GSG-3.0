import pandas as pd
import os
import datetime
from binance_historical_data import BinanceDataDumper
import shutil

def get_kline(frequency, ticker, dateStart, dateEnd):
   
    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump='.',
        asset_class="spot",  
        data_type="klines", 
        data_frequency=frequency,
    )

    data_dumper.dump_data(
        tickers=ticker,
        date_start=datetime.date(year=dateStart[2], 
                                 month=dateStart[1], day=dateStart[0]),
        date_end=datetime.date(year=dateEnd[2], month=dateEnd[1], day=dateEnd[0]),
        is_to_update_existing=False,
        tickers_to_exclude=None
    )

    cwd = os.getcwd();
    date = str(dateStart[0]) + '.' + str(dateStart[1]) + '.' + str(dateStart[2]) + '-' + str(dateEnd[0]) + '.' + str(dateEnd[1])  + '.' + str(dateEnd[2]) + '.csv'
    
    file_path = cwd + '/spot/monthly/klines/' + ticker + '/' + frequency
    output_path = cwd + '/formatted_data/' + ticker +  '/' + frequency + '/' + date
    format_data(file_path, output_path)
    shutil.rmtree(cwd + '/spot')


def format_data(path, out):
    csv_files = os.listdir(path)
    csv_files = [x for x in csv_files if x.lower().endswith('.csv')]
    csv_files = sorted(csv_files)
    df_append = pd.DataFrame()
    for files in csv_files:
        frame = pd.read_csv(path + '/' + files)
        frame = frame.iloc[:, [0,1,2,3,4,5]]
        frame.columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
        frame.timestamp = pd.to_datetime(frame.timestamp, unit='ms')
        frame.set_index('timestamp', inplace=True)
        frame = frame.astype(float)
        df_append = pd.concat([df_append, frame])

    df_append.to_csv(out);

get_kline('1m', 'BTCUSDT', (1, 1, 2021), (1, 1, 2022))
    