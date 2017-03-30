# _*_ coding:utf-8 _*_
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.gevent import GeventScheduler
from API.weather import Weather
from wechat import Operation
from tigger import ContentProduct

sched_block = BlockingScheduler()
sched_gevent = GeventScheduler()


@sched_gevent.scheduled_job('cron', id='weather_job_id', hour=7)
def weather_everyday():
    data = Weather.get(445122, extensions='base')
    msg = ContentProduct.weather_current(data)
    rooms = Operation.search_rooms()
    Operation.send2room(msg, rooms)




