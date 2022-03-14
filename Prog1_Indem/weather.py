import discord
from datetime import date, datetime

color = 0xFF6500
key_features = {
    'description' : 'Description',
    'humidity' : 'Humidity',
    'speed' : 'Speed',
    'temp' : 'Temperature',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}


def extract_data(data):
    all_data = {'description' : data['weather'][0]['description'], 
        'icon' : data['weather'][0]['icon'], 
        'temp' : str(data['main']['temp']) + ' °C', 
        'temp_min' : str(data['main']['temp_min']) + ' °C',
        'temp_max' : str(data['main']['temp_max']) + ' °C',
        'humidity' : str(data['main']['humidity']) + '%',
        'speed' : str(data['wind']['speed']) + ' m/s', 
        'date' : data['dt'], 
        'country' : data['sys']['country']}
    return all_data
    
def weather_message(data, location):
    country = data['country']
    icon = data['icon']
    date = datetime.fromtimestamp(data['date']).strftime('%A, %B %d, %Y %I:%M:%S')
    location = location.title()
    message = discord.Embed(
        title=f'{location}, {country}',
        description=f'{date}',
        color=color
    )
    message.set_thumbnail(url=f'https://openweathermap.org/img/wn/{icon}@2x.png')

    for key in key_features:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=True
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )



