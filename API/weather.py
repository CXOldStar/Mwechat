# _*_ coding:utf-8 _*_
import requests
from API.Const import Const


class Weather:
    REQUEST_URL = 'http://restapi.amap.com/v3/weather/weatherInfo'
    REQUEST_KEY = 'aea2bc7abd9c5ce21f74b368f5010a57'

    def __init__(self, report_province, report_city, report_time, weather_list):
        self.report_provinve = report_province
        self.report_city = report_city
        self.report_time = report_time
        self.weather_list = weather_list

    @staticmethod
    def get(code_city, extensions='all', output='JSON'):
        result = None
        payload = {'key': Weather.REQUEST_KEY, 'city': code_city,
                   'extensions': extensions, 'output': output}
        try:
            response = requests.get(Weather.REQUEST_URL, params=payload, timeout=Const.REQUEST_TIMEOUT)
            if response.status_code == requests.codes.ok:
                response_data = response.json()
                if response_data['status'] == '1' and response_data['infocode'] == '10000':
                    weather_list = []
                    try:
                        if extensions == 'all':
                            weather_data = response_data['forecasts'][0]
                            if len(weather_data['casts']) > 0:
                                for i_weather in weather_data['casts']:
                                    weather_list.append(Weather.Forecast(i_weather))
                        else:
                            weather_data = response_data['lives']
                            weather_list = Weather.Lives(weather_data)
                    except KeyError as e:
                        print('ERROR: %s' % str(e))
                    else:
                        report_time = weather_data['reporttime']
                        report_city = weather_data['city']
                        report_province = weather_data['province']

                        result = Weather(report_province, report_city, report_time, weather_list)
        except requests.exceptions.Timeout as e:
            print('ERROR: %s' % str(e))
        finally:
            return result

    class Forecast:
        def __init__(self, forecast_data):
            self.date = forecast_data['date']
            self.dayweather = forecast_data['dayweather']
            self.nightweather = forecast_data['nightweather']
            self.daytemp = forecast_data['daytemp']
            self.nighttemp = forecast_data['nighttemp']
            self.daypower = forecast_data['daypower']
            self.nightpower = forecast_data['nightpower']

    class Lives:
        def __init__(self, forecast_data):
            self.weather = forecast_data['weather']
            self.temperature = forecast_data['temperature']
            self.winddirection = forecast_data['winddirection']
            self.windpower = forecast_data['windpower']
            self.humidity = forecast_data['humidity']

if __name__ == '__main__':
    data = Weather.get(4404)
    print(data)
