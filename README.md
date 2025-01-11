# CODETECH-TASK_1

**COMPANY** : CODETECH IT SOLUTIONS

**NAME** : Santosh jagan kakde

**INTERN ID** : CT08JNL

**DOMAIN NAME ** : Python Programming

**BATCH DURATIONS** :  5th, 2025 to February 5th, 2025

**MENTOR NAME** : Neela Santhosh Kumar

** Description of the Script and Visualization Dashboard**

Objective:
This Python script fetches weather data from the WeatherAPI (a public API) for multiple cities and creates visualizations using Matplotlib and Seaborn. The goal is to provide a comprehensive and user-friendly weather dashboard that displays key weather parameters, such as temperature, humidity, and pressure, across different cities.

Key Components:
Data Fetching from WeatherAPI:

The script queries the WeatherAPI for the current weather conditions of selected cities, including:
Temperature (in Celsius)
Humidity (in percentage)
Pressure (in millibars)
Weather description (e.g., "Clear", "Cloudy", etc.)
A list of cities (['Pune', 'Kashmir', 'Mumbai', 'New York', 'London']) is used, and the script fetches the data for each city sequentially.
Error Handling:

The script checks if any errors occur during the API request (such as invalid city names or network issues) and prints a relevant error message for each city that could not be fetched.
Data Visualization:

The script creates two types of visualizations:
Bar Charts for temperature, humidity, and pressure:
Temperature (°C) for each city.
Humidity (%) for each city.
Pressure (hPa) for each city.
Line Plot for weather trends:
Temperature and Humidity trends across the selected cities are plotted on the same line graph to compare how these values change from one city to another.
Libraries Used:

requests: To make API requests to the WeatherAPI and fetch weather data.
Matplotlib: To create the bar charts and line plot for visualization.
Seaborn: To enhance the aesthetics of the plots and provide better visual appeal.
Output:

The final output includes:
A set of bar plots that show temperature, humidity, and pressure for each city.
A line plot comparing temperature and humidity across multiple cities, which helps to visualize trends in a comparative manner.
User Interaction:

The script automatically fetches the weather data for a fixed set of cities and displays the weather dashboard.
The visualizations are generated dynamically based on the weather data retrieved from the API.
How to Use the Script:
Step 1: Install necessary libraries (requests, matplotlib, seaborn, pandas) if not already installed:
bash
Copy code
pip install requests matplotlib seaborn pandas
Step 2: Replace the placeholder API key (your_actual_api_key_here) with your actual API key from WeatherAPI.
Step 3: Run the script to fetch weather data and generate the visualizations. The script will produce both bar charts and line plots that give an overview of the weather across the listed cities.
Example Visualization Output:
Bar charts:
The temperature in Celsius, humidity percentage, and pressure in hPa are displayed for each city in individual bars.
Line plot:
A line plot comparing the temperature and humidity for each city, showing the relative trends.
Benefits of the Dashboard:
Data Comparison: The dashboard provides a clear comparison of key weather parameters (temperature, humidity, and pressure) across different cities, helping users quickly understand the weather conditions in different locations.
Easy-to-Understand Visualizations: The use of bar charts and line plots makes the data easy to interpret, even for users with little to no technical background.
Dynamic and Scalable: The script can easily be modified to add more cities or weather parameters, making it scalable for different use cases.



