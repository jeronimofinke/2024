import datetime as dt
import requests
import time
import mysql.connector

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "03a22eb357a47ac53eb73b31e466e998"
CITY = "Emsdetten"

def kelvin_umwandeln(kelvin):
    celsius = kelvin - 273.15
    return celsius

def guardar_en_bd(CITY, temp_celsius):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='temperatura_db'
        )
        cursor = conn.cursor()
        
        fecha = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO temperaturas (ciudad, temperatura, fecha)
            VALUES (%s, %s, %s)
        ''', (CITY, temp_celsius, fecha))
        
        conn.commit()
        print(f"Data inserted: {CITY}, {temp_celsius}, {fecha}")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        cursor.close()
        conn.close()

time.sleep(3)
last_temp_celsius = None
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

while True:
    try:
        response = requests.get(url).json()
        
        if response.get('main'):
            temp_kelvin = response['main']['temp']
            temp_celsius = kelvin_umwandeln(temp_kelvin)
            feels_like_kelvin = response['main']['feels_like']
            feels_like_celcius = kelvin_umwandeln(feels_like_kelvin)
            humidity = response['main']['humidity']
            wind_speed = response['wind']['speed']
            description = response['weather'][0]['description']
            sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
            sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
            
            if last_temp_celsius is None or temp_celsius != last_temp_celsius:
                print(f"Temperatur in {CITY}: {temp_celsius:.2f}°C")
                print(f"Gefühlte Temperatur in {CITY} ist: {feels_like_celcius:.2f}°C")
                print(f"Feuchtigkeit in {CITY}: {humidity:.2f}%")
                print(f"Windgeschwindigkeit in {CITY}: {wind_speed:.2f}m/s")
                print(f"Sonnenaufgang um {sunrise_time}")
                print(f"Sonnenuntergang um {sunset_time}")
                print(f" ")
                fecha = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(fecha)
                guardar_en_bd(CITY, temp_celsius)
                last_temp_celsius = temp_celsius
            
    except Exception as e:
        print(f"Error fetching data: {e}")
    
    time.sleep(15)
