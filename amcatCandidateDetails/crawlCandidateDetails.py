import urllib.request
import  time
import locale
import os

from django.http import HttpResponse
from django.utils.encoding import smart_str

"""changing dir in this file also leads to change in 'CWDir' of parent scripts, like 'my attempt' """
EX_DIR = os.getcwd()
# os.makedirs(EX_DIR + '/candidateDetails')
os.chdir(EX_DIR + '/candidateDetails')

def pullDetails(orderId, count):
    # print('current working dir : ' + os.getcwd())
    if orderId is None:
        orderId = "02027982"
    if count is None:
        count = 5
    fileName = ''
    try:
        fileName = 'CandidateDetails_' + orderId + '_' +  str(count) + '.txt'
        with open(fileName, 'w')  as fw:                    # we open file in write mode rather than append mode so that if we run this script accidently AAPL.txt is updated with valid no of rows, important for other project files
            for i in range(int(orderId), int(orderId) + int(count)):
                url = 'http://backend.myamcat.com/displayAdmitCard.php?orderId=' + str(i)
                source =  urllib.request.urlopen(url).read()
                encoding = locale.getdefaultlocale()[1]
                splitSource = source.decode(encoding).split('\n')
                orderIdDoesNotExistStrs = splitSource[33].split('Order ID not found..')
                if len(orderIdDoesNotExistStrs) > 1:  # means str 'Order ID not found..' is present in splitSource[33]
                    fw.write(orderId + ': Order ID not found..\n')
                else:
                    fw.write(orderId + ': ' + splitSource[53].split('</strong>: ')[1] + ', ' + splitSource[56].split(':</strong> ')[1] + ', ' + splitSource[59].split(':</strong> ')[1] + '\n')
            print('Successfully Pulled Details')
            return fileName

    except (Exception) as e:
        print('main loop : ', str(e))

def download_file(file_name):
    path_to_file = EX_DIR + '\\candidateDetails\\' + file_name
    my_file = open(path_to_file, 'rb').read()
    response = HttpResponse(my_file, content_type = "text/html")
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response
