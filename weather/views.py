from datetime import datetime
from re import search
from turtledemo.penrose import start

from django.conf import settings
from django.shortcuts import render
import requests
from pyexpat.errors import messages


# Create your views here.
def index(request):
    location = 'Moscow'
    if 'location_input' in request.POST:
        location = request.POST['location_input']
    open_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid=bcab89ad8807c1e58030b852f013ab28&units=metric'
    image_url = ''
    try:
        SEARCH_API = ''
        SEACH_ENGINE_ID = ''
        query = location + ' 1920x1080'
        location_url = f'https://www.googleapis.com/customsearch/v1?key={SEARCH_API}&cx={SEACH_ENGINE_ID}&q={query}&searchType=image'
        data = requests.get(location_url).json()
        search_items = data.get('items')
        for item in search_items:
            access = requests.get(item['link']).status_code
            if access==200:
                image_url = item['link']
                break
            else:
                continue    
        
    except Exception as e:
        print(f'Ошибка google: {e}')
        
    try:

        data = requests.get(open_weather_url).json()

        context = {
            'location': location,
            'description': data['weather'][0]['description'],
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'icon': data['weather'][0]['icon'],
            'wind': data['wind']['speed'],
            'feels_like': data['main']['feels_like'],
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'image_url': image_url,
            
        }
        return render(request, 'weather.html', context)
    except Exception as e:
        print(f'Ошибка: {e}')
        context = {
            'location': location,
            'description': '',
            'temp': '',
            'humidity': '',
            'pressure': '',
            'icon': '01d',
            'wind': '',
            'feels_like': '',
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'image_url': image_url,
            
        }
        return render(request, 'weather.html', context)
