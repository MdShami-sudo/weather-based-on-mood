import tkinter as tk
from tkinter import messagebox
import random

class WeatherMoodChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Weather Checker Based on Mood")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="What's your mood today?", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.mood_var = tk.StringVar()
        self.mood_entry = tk.Entry(root, textvariable=self.mood_var, font=("Arial", 12), width=25)
        self.mood_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Weather", font=("Arial", 12), bg="#4caf50", fg="#ffffff", command=self.check_weather)
        self.check_button.pack(pady=10)

        self.weather_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.weather_label.pack(pady=10)

    def check_weather(self):
        mood = self.mood_var.get().lower()
        weather = self.get_random_weather(mood)
        self.weather_label.config(text=f"The weather for your mood ({mood}): {weather}")

    def get_random_weather(self, mood):
        weather_conditions = {
            "happy": ["Sunny", "Clear Skies", "Warm and Pleasant"],
            "sad": ["Rainy", "Cloudy", "Cold and Windy"],
            "angry": ["Stormy", "Thunderstorms", "Heavy Rain"],
            "relaxed": ["Mild", "Partly Cloudy", "Cool Breeze"],
            "excited": ["Bright Sunshine", "Clear", "Hot and Energetic"]
        }
        
        default_weather = ["Mixed Weather", "Unpredictable", "Varied Conditions"]
        return random.choice(weather_conditions.get(mood, default_weather))

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherMoodChecker(root)
    root.mainloop()
