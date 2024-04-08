from weather_data.models import Weather
import logging
import requests
from datetime import datetime, timedelta
from requests.exceptions import HTTPError


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
        "X-RapidAPI-Key": "66dcbafb75msha536f3086b06788p1f5e7ajsnac1315877f0f",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        logger.info(f"here")
        if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)
            forecast = weather_data.get("forecast", None)
            if forecast:
                forecastday = forecast.get("forecastday", None)
                print(forecastday)
                # if forecastday[0]:
                #     hour = forecastday[0].get("hour", None)
                #     if hour:
                #         time = hour[0].get("time", None)
                #         temp = hour[0].get("temp_c", None)
                #         clouds = hour[0].get("cloud", None)
                #         heatindex = hour[0].get("heatindex_c", None)
                #         uv = hour[0].get("uv", None)
                #         if time and temp and clouds and heatindex and uv:
                #             exist = Weather.objects.filter(timestamp=time, lat=lat,long=long)
                #             if not exist:
                #                 Weather.objects.create(timestamp=time, temperature=temp, clouds=clouds, heatindex=heatindex, lat=lat, long=long, uv=uv)
         
    except HTTPError as http_err:
        logger.info(f"HTTP error occurred: {http_err}")




def fill_history_data():
    count = -1
    today = datetime.now() 
    for i in range(2):
        count += 1
        one_hour_before = today - timedelta(hours=count)   
        date_part = one_hour_before.strftime('%Y-%m-%d')
        hour_part = one_hour_before.strftime('%H')
        make_weather_request(date_part, hour_part)        
        
        logger.info(f"{date_part} {hour_part}")
    

