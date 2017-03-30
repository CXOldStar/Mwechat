# _*_ coding:utf-8 _*_


class ContentProduct:

    @staticmethod
    def weather_current(data):
        weather = data.weather_list
        return '%s当前气象简报：室外温度%s 天气主要是%s 空气湿度%s (%s)' \
               % (data.report_provinve+data.report_city,
                  weather.temperature, weather.weather, weather.humidity,
                  data.report_time)

