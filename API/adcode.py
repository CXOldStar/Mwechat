# _*_ coding:utf-8 _*_
import requests
from API.Const import Const


class Adcode:
    REQUEST_URL = 'http://restapi.amap.com/v3/geocode/geo'
    REQUEST_KEY = 'e2f5058c737e45f014d0a698747c754d'

    def __init__(self, query_address, adcode):
        self.query_address = query_address
        self.adcode = adcode

    @staticmethod
    def get(address, output='JSON'):
        result = None
        payload = {'key': Adcode.REQUEST_KEY, 'address': address, 'batch': 'true', 'output': output}
        try:
            response = requests.get(Adcode.REQUEST_URL, params=payload, timeout=Const.REQUEST_TIMEOUT)
            if response.status_code == requests.codes.ok:
                response_data = response.json()
                if response_data['status'] == '1' and response_data['infocode'] == '10000':
                    count = response_data['count']
                    if int(count) == 0:
                        pass
                    elif int(count) > 1:
                        result = count
                    else:
                        data = response_data['geocodes'][0]
                        query_address = data['formatted_address']
                        adcode = data['adcode']
                        result = Adcode(query_address, adcode)
        except requests.exceptions.Timeout as e:
            print('ERROR: %s' % str(e))
        finally:
            return result


if __name__ == '__main__':

    data = Adcode.get('饶平县')
    print(data.adcode)
