import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to fetch weather data for a given city
def fetch_weather_data(city):
    # Update the URL for WeatherAPI
    URL = f'http://api.weatherapi.com/v1/current.json?key=0a5b3e08647049d8ac891021251101&q={city}&aqi=no'
    response = requests.get(URL)
    data = response.json()
    
    # Check for errors in the response
    if 'error' in data:
        print(f"Error fetching data for {city}: {data['error']['message']}")
        return None
    
    # Extract relevant weather data
    weather_info = {
        'city': city,
        'temperature': data['current']['temp_c'],  # Temperature in Celsius
        'humidity': data['current']['humidity'],   # Humidity in percentage
        'pressure': data['current']['pressure_mb'],  # Pressure in millibars
        'description': data['current']['condition']['text']  # Weather description
    }
    return weather_info

# Function to fetch weather data for multiple cities
def fetch_multiple_weather_data(cities):
    weather_data = []
    for city in cities:
        city_data = fetch_weather_data(city)
        if city_data:
            weather_data.append(city_data)
    return weather_data

# Function to create bar plot for the weather data
def plot_weather_data(weather_data):
    if not weather_data:
        print("No valid weather data to plot.")
        return
    
    # Create a DataFrame for visualization
    df = pd.DataFrame(weather_data)
    
    # Plot the temperature, humidity, and pressure for each city
    df.set_index('city', inplace=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 6), sharey=True)
    
    # Temperature Plot
    sns.barplot(x=df.index, y='temperature', data=df, ax=axes[0], palette='Blues')
    axes[0].set_title('Temperature (°C)')
    
    # Humidity Plot
    sns.barplot(x=df.index, y='humidity', data=df, ax=axes[1], palette='Greens')
    axes[1].set_title('Humidity (%)')
    
    # Pressure Plot
    sns.barplot(x=df.index, y='pressure', data=df, ax=axes[2], palette='Reds')
    axes[2].set_title('Pressure (hPa)')

    # Display the plot
    plt.tight_layout()
    plt.show()

# Function to create weather trend pie chart (weather conditions across cities)
def plot_weather_condition_pie(weather_data):
    conditions = [data['description'] for data in weather_data]
    condition_counts = pd.Series(conditions).value_counts()
    
    # Pie chart for weather conditions
    plt.figure(figsize=(7, 7))
    plt.pie(condition_counts, labels=condition_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set2', len(condition_counts)))
    plt.title('Weather Conditions Across Cities')
    plt.show()

# Function to create a heatmap showing temperature, humidity, and pressure across cities
def plot_weather_heatmap(weather_data):
    if not weather_data:
        print("No valid weather data to plot.")
        return
    
    # Create a DataFrame for heatmap
    df = pd.DataFrame(weather_data)
    df.set_index('city', inplace=True)
    
    # Heatmap for temperature, humidity, and pressure
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[['temperature', 'humidity', 'pressure']], annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Weather Data Heatmap')
    plt.show()

# Function to create scatter plots for temperature vs humidity and pressure vs temperature
def plot_weather_scatter(weather_data):
    if not weather_data:
        print("No valid weather data to plot.")
        return
    
    # Create a DataFrame for visualization
    df = pd.DataFrame(weather_data)
    
    # Scatter plot for Temperature vs Humidity
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temperature', y='humidity', data=df, hue='city', palette='Set2', s=100)
    plt.title('Temperature vs Humidity')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Humidity (%)')
    plt.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    # Scatter plot for Pressure vs Temperature
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temperature', y='pressure', data=df, hue='city', palette='Set1', s=100)
    plt.title('Pressure vs Temperature')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Pressure (hPa)')
    plt.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Main function to create the weather dashboard
def create_weather_dashboard(cities):
    # Fetch weather data for the cities
    weather_data = fetch_multiple_weather_data(cities)

    # Plot bar charts for temperature, humidity, and pressure
    plot_weather_data(weather_data)
    
    # Plot pie chart for weather conditions
    plot_weather_condition_pie(weather_data)
    
    # Plot heatmap for weather data
    plot_weather_heatmap(weather_data)
    
    # Plot scatter plots for temperature vs humidity and pressure vs temperature
    plot_weather_scatter(weather_data)

# List of cities to fetch weather data for
cities = ['Pune', 'Kashmir', 'Mumbai', 'New York', 'London']

# Create the weather dashboard
create_weather_dashboard(cities)
