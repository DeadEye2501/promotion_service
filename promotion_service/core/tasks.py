from dateutil.relativedelta import relativedelta
from celery import shared_task
from .utils import *


@shared_task
def check_polygon_api():
    get_values(str((datetime.now()-relativedelta(years=1)).date()), str(datetime.now().date()))
