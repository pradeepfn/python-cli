import logging
import http.client
from multiprocessing import connection

__author__ = 'pradeep'

log = logging.getLogger(__name__)


def getTenants(self):
    send_receive('GET','/list/tenant',None)


def send_receive(self, httpMethod, endpointContext, payload):
    endpoint = '/stratos' + endpointContext
    connection = http.client.HTTPConnection('127.0.0.1','9763')
    headers = {"Content-type": "application/json",
               "Accept": "application/json"}
    connection.request(httpMethod,endpoint,payload,headers)
    response = connection.getresponse()
    print(response.status,response.reason)
    connection.close()
