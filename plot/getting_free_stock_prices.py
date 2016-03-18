""""http://chartapi.finance.yahoo.com/instrument/1.0/AAPL/chartdata;type=quote;range=1y/csv"""
# try:
#     import urllib.request as urllib2
# except ImportError:
#     import urllib2
import urllib.request
import  time
import locale
import os
import  sys
"""changing dir in this file also leads to change in 'CWDir' of parent scripts, like 'my attempt' """
# EX_DIR = os.getcwd() + '/polls/'
# os.chdir(EX_DIR + '/stocks pulled')
EX_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\stocks pulled\\"

def pullData(stock):
    # print('current working dir : ' + os.getcwd())
    try:
        url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        source =  urllib.request.urlopen(url).read()
        encoding = locale.getdefaultlocale()[1]
        # print(encoding)
        splitSource = source.decode(encoding).split('\n')
        fw = open(EX_DIR + stock + '.txt', 'w')                      # we open file in write mode rather than append mode so that if we run this script accidently AAPL.txt is updated with valid no of rows, important for other project files
        for lines in splitSource:
            line = lines.split(',')
            if len(line) == 6:
                if line[0] != 'values:Date':
                    data = lines + '\n'
                    fw.write(data)
        print('Pulled : ' + stock)

        # time.sleep(1)               #halt execuztion for 1 sec, not needed jst learn the use

    except (Exception) as e:
        print("\nmain loop : ", str(e), "\n" )

# stock = input('enter the stock to be pulled : ')
# pullData(stock)