import threading

__author__ = 'Sony'
import time
import datetime

import django

from numpy import  *
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
from matplotlib.finance import *                    # we need candlestick_ochl
import matplotlib
# matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from . import getting_free_stock_prices
matplotlib.rcParams.update({'font.size' : 10})
import pylab
import sys
import os
from multiprocessing.pool import ThreadPool
EX_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\stocks pulled\\"

def sma(close, window):
    fraction = repeat(1.0, window)/window
    return convolve(close, fraction, 'valid')

def rsi(prices, n):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range (n, len(prices)):
        if deltas[i-1] > 0 :
            upval = deltas[i-1]
            downval = 0.
        else:
            upval = 0.
            downval = -deltas[i-1]

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

# def pullData(s):
#     """pull stock data"""
#     stock = s
#     getting_free_stock_prices.pullData(stock)
#     return stock

pool = ThreadPool(processes=1)
def threadBoy(stock):
    # t=threading.Thread(target=plotData,args=(stock,))
    async_result = pool.apply_async(plotData, args=(stock,))
    return async_result.get()

def plotData(stock):
    getting_free_stock_prices.pullData(stock)
    """extract data - ochlv in float format"""
    data = genfromtxt(EX_DIR + '/' + stock + '.txt', delimiter=',', dtype = float)
    close, high, low, open, vol = data[:, 1], data[:, 2], data[:, 3], data[:, 4], data[:, 5]
    """extract dates in str format"""
    data = genfromtxt(EX_DIR + '/' + stock + '.txt', delimiter=',', dtype = str)
    data = data[:, 0]
    # print(data[:, 0])
    dates = []
    data_for_candle = []

    """convert dates from str to datetime.datetime"""
    for d in range(0, shape(data)[0]):
        dates.append(datetime.datetime(int(data[d][0:4]), int(data[d][4:6]), int(data[d][6:8])))
        line_to_append = mdates.date2num(dates[d]), open[d], close[d], high[d], low[d], vol[d]
        data_for_candle.append(line_to_append)

    """preapare to plot data"""
    fig = plt.figure(stock)

    """divide the screen in 5 rows 4 cols, start ax1 at (0, 0)"""
    ax1 = plt.subplot2grid((5, 4), (0, 0), colspan=4, rowspan=4)
    ax1.grid(True)
    candlestick_ochl(ax1, data_for_candle,  width=1, colorup = 'g', colordown='r')

    ax1.spines['top'].set_color('white')

    """moving averages"""
    # ma = input('enter the type of moving avg to be analysed : \n 1.simple moving avg \n 2.exponential moving avg')
    ma = 1
    # a, b = input('enter the two durations for which moving averages are to be analysed : ')
    a, b = 52, 26

    if ma is 1:
        avg_a = sma(close, a)
        avg_b = sma(close, b)

        strt = int((a-1)/2)
        end = shape(avg_a)[0] + strt
        y = []
        ax1.xaxis.set_ticklabels(y)
        p1 = ax1.plot(dates[strt : end] , avg_a, label=str(a) + ' Day SMA')
        # maLeg = plt.legend(loc = 5, ncol=2, prop={'size':19}, fancybox=True, borderaxespad=0.)
        # maLeg.get_frame().set_alpha(0.4)
        # textEd = pylab.gca().get_legend().get_texts()
        # pylab.setp(textEd[0:5], color = 'p')
        strt = int((b-1)/2)
        end = shape(avg_b)[0] + strt
        p2 = ax1.plot(dates[strt : end] , avg_b, label=str(b) + ' Day SMA')
        plt.xlabel('dates')
        plt.ylabel('stock price')

    """volume"""
    """have to set ax2 before plotting sma, as going odr way around, upsets legends,,  ... ??"""
    ax2 = ax1.twinx()
    p3 = ax2.plot(dates, vol, color='#00ffe8', linewidth=0.8, label='volume')
    ax2.fill_between(dates, 0, vol, facecolor='#00ffe8', alpha=0.5)
    ax2.set_ylim(0, 5*vol.max())

    """rsi"""
    ax3 = plt.subplot2grid((5, 4), (4, 0), colspan=4, rowspan=1)
    ax3.set_yticks([30, 70])
    plt.ylabel("RSI")

    p4 = plt.plot(dates, rsi(close, 14), label='20 day rsi')
    ax3.axhline(30)
    ax3.axhline(70)
    # plt.gca().yaxis.set_major_locator(mtick.MaxNLocator(10))


    """plot data"""
    """combine lehends"""
    ax = p1 + p2 + p3
    l = [x.get_label() for x in ax]
    ax1.legend(ax, l, loc=0)

    l = [x.get_label() for x in p4]
    ax3.legend(ax, l, loc=0)

    """adjust xaxis.set_ticklabels()"""
    ax3.xaxis.set_major_locator(mtick.MaxNLocator(10))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%y"))
    for d in ax3.xaxis.get_ticklabels():
        d.set_rotation(45)

    plt.subplots_adjust(left=0.08, bottom=0.10, right=0.95, top=0.95, hspace=0.0)
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)

    # plt.show()
    # plt.close()
    # sys.stderr.write('%%%%%%%%%%%%%%%%%%%%')
    return response
    # ax1.plot(dates, open)


# threadBoy('GOOG')


"""             ***         USING COMMANDLINE ARGS          ***         """
# def main(s):
#     plotData(s)


# if __name__ == "__main__":
#   args = sys.argv
#   main(args)
