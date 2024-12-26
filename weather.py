import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != "404":
            main_data = data["main"]
            weather_data = data["weather"][0]
            
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            description = weather_data["description"]
            
            result_label.config(text=f"Temperature: {temperature}°C\n"
                                    f"Pressure: {pressure} hPa\n"
                                    f"Humidity: {humidity}%\n"
                                    f"Description: {description.capitalize()}")
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 14))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14), command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="Weather details will appear here.", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()

