import requests
import os

AIO_USERNAME = "Vinhnguyen20"
AIO_KEY = ""
AIO_FEED_ID = "update-CI_CD"

def send_update_message():
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED_ID}/data"
    headers = {
        "X-AIO-Key": AIO_K,
        "Content-Type": "application/json"
    }
    data = {"value": "update"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} {response.text}")

if __name__ == "__main__":
    send_update_message()
