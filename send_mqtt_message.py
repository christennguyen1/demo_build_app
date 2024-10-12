import requests
import os

AIO_USERNAME = os.getenv("AIO_USERNAME")  # Tên người dùng Adafruit IO từ env
AIO_K = os.getenv("AIO_KEY")  # API Key lấy từ GitHub Secrets qua env
AIO_FEED_ID = "cicd"  # Feed ID chính xác

def send_update_message():
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED_ID}/data"
    headers = {
        "X-AIO-Key": AIO_K,
        "Content-Type": "application/json"
    }
    version = "2.1.12"
    data = {"value": f"update version {version}"}  # Dữ liệu gửi lên
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} {response.text}")

if __name__ == "__main__":
    send_update_message()
