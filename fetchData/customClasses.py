import pandas as pd
import plotly.graph_objs as go
import talib
import numpy as np

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import dash

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///multiple_stocks.db"
CORS(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')

db = SQLAlchemy(server)


class Graph:
    def __init__(self, graphName, datepicker, timespan):
        self.graphName = graphName
        self.datepicker = datepicker
        self.timespan = timespan
        self.df = self.generateData()
        self.indicators = []

    def generateData(self):
        print('GenerateData')
        df = pd.read_sql_table(table_name=self.graphName, con=db.engine)

        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        #
        ohlc_dict = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'}
        df = df.resample(self.timespan).agg(ohlc_dict).dropna(how='any')

        return df

    def graphBase(self, graphType):
        if graphType == 'Scatter':
            return getattr(go, graphType)(
                x=self.df.index,
                y=self.df.close,
                name=f'{self.graphName}' + ' graphType',
            )

        return getattr(go, graphType)(
            x=self.df.index,
            open=self.df.open,
            high=self.df.high,
            low=self.df.low,
            close=self.df.close,
            name=f'{self.graphName}' + graphType,
        )

    def SMA(self, timeperiod=14):
        real_close = np.array(self.df.close, dtype='f8')
        sma = talib.SMA(np.asarray(real_close), timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=sma,
        #     name='SMA'
        # )
        return sma

    def WILLR(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        willr = talib.WILLR(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=willr,
        #     name='WILLR'
        # )
        return willr

    # ADX - Average Directional Movement Index
    def ADX(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        adx = talib.ADX(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=adx,
        #     name='ADX'
        # )
        return adx

    # ADXR - Average Directional Movement Index Rating
    def ADXR(self, indicatorSpan=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        adxr = talib.ADXR(real_data[0], real_data[1], real_data[2], timeperiod=indicatorSpan)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=adxr,
        #     name='ADXR'
        # )
        return adxr

    # APO - Absolute Price Oscillator
    def APO(self, fastPeriod=12, slowPeriod=26, matype=0):
        real_data = np.array([self.df.close], dtype='f8')
        apo = talib.APO(real_data[0], fastperiod=fastPeriod, slowperiod=slowPeriod, matype=matype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=apo,
        #     name='APO'
        # )
        return apo

    # AROON - Aroon
    def AROON(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low], dtype='f8')
        # aroondown, aroonup = talib.AROON(real_data[0], real_data[1], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=aroondown,
        #     name='AROON'
        # )
        return talib.AROON(real_data[0], real_data[1], timeperiod=timeperiod)

    # AROONOSC - Aroon Oscillator
    def AROONOSC(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low], dtype='f8')
        aroonosc = talib.AROONOSC(real_data[0], real_data[1], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=aroonosc,
        #     name='AROONOSC'
        # )
        return aroonosc

    # BOP - Balance Of Power
    def BOP(self):
        real_data = np.array([self.df.open, self.df.high, self.df.low, self.df.close], dtype='f8')
        bop = talib.BOP(real_data[0], real_data[1], real_data[2], real_data[3])
        # return go.Scatter(
        #     x=self.df.index,
        #     y=bop,
        #     name='BOP'
        # )
        return bop

    # CCI - Commodity Channel Index
    def CCI(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        cci = talib.CCI(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=cci,
        #     name='CCI'
        # )
        return cci

    # CMO - Chande Momentum Oscillator
    def CMO(self, timeperiod=14):
        real_data = np.array([self.df.close], dtype='f8')
        cmo = talib.CMO(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=cmo,
        #     name='CMO'
        # )
        return cmo

    # DX - Directional Movement Index
    def DX(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        dx = talib.DX(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=dx,
        #     name='DX'
        # )
        return dx

    # Doubts starting here!!
    # MACD - Moving Average Convergence / Divergence
    def MACD(self, fastperiod=12, slowperiod=26, signalperiod=9):
        real_data = np.array([self.df.close], dtype='f8')
        # macd, macdsignal, macdhist = talib.MACD(real_data[0], fastperiod=fastperiod, slowperiod=slowperiod,
        #                                         signalperiod=signalperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=macd,
        #     name='MACD'
        # )
        return talib.MACD(real_data[0], fastperiod=fastperiod, slowperiod=slowperiod,
                          signalperiod=signalperiod)

    # MACDEXT - MACD with controllable MA type
    def MACDEXT(self, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        real_data = np.array([self.df.close], dtype='f8')
        # macd, macdsignal, macdhist = talib.MACDEXT(real_data[0], fastperiod=fastperiod, fastmatype=fastmatype,
        #                                            slowperiod=slowperiod,
        #                                            slowmatype=slowmatype, signalperiod=signalperiod,
        #                                            signalmatype=signalmatype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=macd,
        #     name='MACDEXT'
        # )
        return talib.MACDEXT(real_data[0], fastperiod=fastperiod, fastmatype=fastmatype,
                             slowperiod=slowperiod,
                             slowmatype=slowmatype, signalperiod=signalperiod,
                             signalmatype=signalmatype)

    # MACDFIX - Moving Average Convergence / Divergence Fix 12 / 26
    def MACDFIX(self, signalperiod=9):
        real_data = np.array([self.df.close], dtype='f8')
        # macd, macdsignal, macdhist = talib.MACDFIX(real_data[0], signalperiod=signalperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=macd,
        #     name='MACDFIX'
        # )
        return talib.MACDFIX(real_data[0], signalperiod=signalperiod)

    # MFI - Money Flow Index
    def MFI(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close, self.df.volume], dtype='f8')
        mfi = talib.MFI(real_data[0], real_data[1], real_data[2], real_data[3], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=mfi,
        #     name='MFI'
        # )
        return mfi

    # MINUS_DI - Minus Directional Indicator
    def MINUS_DI(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        minus_di = talib.MINUS_DI(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=minus_di,
        #     name='MINUS_DI'
        # )
        return minus_di

    # MINUS_DM - Minus Directional Movement
    def MINUS_DM(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low], dtype='f8')
        minus_dm = talib.MINUS_DM(real_data[0], real_data[1], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=minus_dm,
        #     name='MINUS_DM'
        # )
        return minus_dm

    # MOM - Momentum
    def MOM(self, timeperiod=10):
        real_data = np.array([self.df.close], dtype='f8')
        mom = talib.MOM(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=mom,
        #     name='MOM'
        # )
        return mom

    # PLUS_DI - Plus Directional Indicator
    def PLUS_DI(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        plus_di = talib.PLUS_DI(real_data[0], real_data[1], real_data[2], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=plus_di,
        #     name='PLUS_DI'
        # )
        return plus_di

    # PLUS_DM - Plus Directional Movement
    def PLUS_DM(self, timeperiod=14):
        real_data = np.array([self.df.high, self.df.low], dtype='f8')
        plus_dm = talib.PLUS_DM(real_data[0], real_data[1], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=plus_dm,
        #     name='PLUS_DM'
        # )
        return plus_dm

    # PPO - Percentage Price Oscillator
    def PPO(self, fastperiod=12, slowperiod=26, matype=0):
        real_data = np.array([self.df.close], dtype='f8')
        ppo = talib.PPO(real_data[0], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=ppo,
        #     name='PPO'
        # )
        return ppo

    # ROC - Rate of change: ((price / prevPrice) - 1) * 100
    def ROC(self, timeperiod=10):
        real_data = np.array([self.df.close], dtype='f8')
        roc = talib.ROC(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=roc,
        #     name='ROC'
        # )
        return roc

    # ROCP - Rate of change Percentage: (price - prevPrice) / prevPrice
    def ROCP(self, timeperiod=10):
        real_data = np.array([self.df.close], dtype='f8')
        rocp = talib.ROCP(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=rocp,
        #     name='ROCP'
        # )
        return rocp

    # ROCR - Rate of change ratio: (price / prevPrice)
    def ROCR(self, timeperiod=10):
        real_data = np.array([self.df.close], dtype='f8')
        rocr = talib.ROCR(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=rocr,
        #     name='ROCR'
        # )
        return rocr

    # ROCR100 - Rate of change ratio 100 scale: (price / prevPrice) * 100
    def ROCR100(self, timeperiod=10):
        real_data = np.array([self.df.close], dtype='f8')
        rocr100 = talib.ROCR100(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=rocr100,
        #     name='ROCR100'
        # )
        return rocr100

    # RSI - Relative Strength Index
    def RSI(self, timeperiod=14):
        real_data = np.array([self.df.close], dtype='f8')
        rsi = talib.RSI(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=rsi,
        #     name='RSI'
        # )
        return rsi

    # STOCH - Stochastic
    def STOCH(self, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        # slowk, slowd = talib.STOCH(real_data[0], real_data[1], real_data[2], fastk_period=fastk_period,
        #                            slowk_period=slowk_period, slowk_matype=slowk_matype, slowd_period=slowd_period,
        #                            slowd_matype=slowd_matype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=slowk,
        #     name='STOCH'
        # )
        return talib.STOCH(real_data[0], real_data[1], real_data[2], fastk_period=fastk_period,
                           slowk_period=slowk_period, slowk_matype=slowk_matype, slowd_period=slowd_period,
                           slowd_matype=slowd_matype)

    # STOCHF - Stochastic Fast
    def STOCHF(self, fastk_period=5, fastd_period=3, fastd_matype=0):
        real_data = np.array([self.df.high, self.df.low, self.df.close], dtype='f8')
        # fastk, fastd = talib.STOCHF(real_data[0], real_data[1], real_data[2], fastk_period=fastk_period,
        #                             fastd_period=fastd_period, fastd_matype=fastd_matype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=fastk,
        #     name='STOCHF'
        # )
        return talib.STOCHF(real_data[0], real_data[1], real_data[2], fastk_period=fastk_period,
                            fastd_period=fastd_period, fastd_matype=fastd_matype)

    # STOCHRSI - Stochastic Relative Strength Index
    def STOCHRSI(self, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
        real_data = np.array([self.df.close], dtype='f8')
        # fastk, fastd = talib.STOCHRSI(real_data[0], timeperiod=timeperiod, fastk_period=fastk_period,
        #                               fastd_period=fastd_period, fastd_matype=fastd_matype)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=fastk,
        #     name='STOCHRSI'
        # )
        return talib.STOCHRSI(real_data[0], timeperiod=timeperiod, fastk_period=fastk_period,
                              fastd_period=fastd_period, fastd_matype=fastd_matype)

    # TRIX - 1 - day Rate - Of - Change(ROC) of a Triple Smooth EMA
    def TRIX(self, timeperiod=30):
        real_data = np.array([self.df.close], dtype='f8')
        trix = talib.TRIX(real_data[0], timeperiod=timeperiod)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=trix,
        #     name='TRIX'
        # )
        return trix

    # ULTOSC - Ultimate Oscillator
    def ULTOSC(self, timeperiod1=7, timeperiod2=14, timeperiod3=28):
        real_data = np.array([self.df.close], dtype='f8')
        ultosc = talib.ULTOSC(real_data[0], timeperiod1=timeperiod1, timeperiod2=timeperiod2, timeperiod3=timeperiod3)
        # return go.Scatter(
        #     x=self.df.index,
        #     y=ultosc,
        #     name='ULTOSC'
        # )
        return ultosc


if __name__ == '__main__':
    pass
