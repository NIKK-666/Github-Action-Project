import requests

def get_weather():
    # Using a free, no-auth API for simplicity
    city = "Bilaspur"
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Current Weather Report: {response.text}")
        else:
            print("Failed to fetch weather data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_weather()