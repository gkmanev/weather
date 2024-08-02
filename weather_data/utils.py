from weather_data.models import Weather
import logging
import requests
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from pytz import timezone

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set to DEBUG for detailed logging



def make_weather_request(date, hour):
    url = "https://weatherapi-com.p.rapidapi.com/history.json"
    lat = 43.2265
    long = 27.9504
    querystring = {
        "q":f"{lat}, {long}",
        "dt":date,
        "lang":"en",
        "hour":hour
        }
    headers = {
        "X-RapidAPI-Key": "b3987e9030mshdc8782a497a2fb2p1c6f2fjsnad1c1b9ddd22",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            forecast = weather_data.get("forecast", None)
            if forecast:
                forecastday = forecast.get("forecastday", None)
                
                if forecastday[0]:
                    hour = forecastday[0].get("hour", None)
                    if hour:
                        time = hour[0].get("time", None)                        
                        temp = hour[0].get("temp_c", None)
                        clouds = hour[0].get("cloud", None)
                        heatindex = hour[0].get("heatindex_c", None)
                        uv = hour[0].get("uv", None)
                        logger.info(f"TEMP:{temp}")
                        if time and temp and clouds and heatindex and uv:
                            exist = Weather.objects.filter(timestamp=time, lat=lat,long=long)
                            logger.info(exist)
                            if not exist:
                                logger.info(f"Temperature: {temp}")
                                Weather.objects.create(timestamp=time, temperature=temp, clouds=clouds, heatindex=heatindex, lat=lat, long=long, uv=uv)
         
    except HTTPError as http_err:
        logger.info(f"HTTP error occurred: {http_err}")




def fill_history_data():
    count = -1   
    today = datetime.now(timezone('Europe/Sofia'))
    print(today)
    for i in range(1):
        count += 1
        one_hour_before = today - timedelta(hours=count)   
        date_part = one_hour_before.strftime('%Y-%m-%d')
        hour_part = one_hour_before.strftime('%H')
        make_weather_request(date_part, hour_part)        
        
        logger.info(f"{date_part} {hour_part}")
    

