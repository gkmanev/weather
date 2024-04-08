# weather_data/tasks.py
from celery import shared_task
from weather_data.utils import fill_history_data
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set to DEBUG for detailed logging


@shared_task
def update_weather_data_task():
    fill_history_data()
    logger.info("Update history data")