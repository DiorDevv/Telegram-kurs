import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

async def get_weather(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=uz"
    )
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                name = data["name"]
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                return (
                    f"📍 Shahar: {name}\n"
                    f"🌡 Harorat: {temp}°C\n"
                    f"🌥 Ob-havo: {weather}\n"
                    f"💧 Namlik: {humidity}%\n"
                    f"🌬 Shamol: {wind} m/s"
                )
            else:
                return "❌ Bunday shahar topilmadi. Iltimos, to'g'ri kiriting."
