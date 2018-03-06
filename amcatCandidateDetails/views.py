import sys

from amcatCandidateDetails import crawlCandidateDetails

def scrapDetails(self, orderId, count):
    sys.stderr.write('\n*****************\n')
    sys.stderr.write(orderId + ', ' + count)
    sys.stderr.write('\n*****************\n')
    fileName = crawlCandidateDetails.pullDetails(orderId, count)
    return  crawlCandidateDetails.download_file(fileName)