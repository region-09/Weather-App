from django.http import JsonResponse
from django.shortcuts import render
import requests


API_KEY = "17d6cff64590fb740938a79e9ec74c27"

def weather_data(request):
    # используем POST request для имени города
    # если пользователь напишет Bishkek в index.html то request.POST['city'] равен Bishkek
    if request.method == 'POST' and request.POST['city'].strip() != '':
        url = f"http://api.openweathermap.org/data/2.5/weather?q={request.POST['city'].strip()}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        # print(data)
        # Если у нас есть успешное подключение
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            return render(request, 'index.html', {
                "temperature": temperature,
                "pressure": pressure,
                "wind_speed": wind_speed,
                "city": request.POST['city'].strip(),
            })
        # Не успешное подлючение или проблемы в имени города
        else:
            return render(request, 'templates/index.html', {"error": "Не удалось найти Город или проблемы с сервером или с вашим интернетом"})
    else:
        return render(request, 'templates/index.html', {})