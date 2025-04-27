import requests
import json

# URL API server Flask đang chạy
url = "http://127.0.0.1:5000/predict"

# Dữ liệu mẫu để predict
data = {
    "feature_0": 2.5,
    "feature_1": 1.8,
    "feature_2": 2.1,
    "feature_3": 3.0,
    "feature_4": 2.7,
    "feature_5": 2.4,
    "feature_6": 1.9,
    "feature_7": 2.8,
    "feature_8": 2.2,
    "feature_9": 2.0
}

# Gửi request POST
response = requests.post(url, json=data)

# In kết quả ra màn hình
if response.status_code == 200:
    print("✅ Predict thành công!")
    print("Kết quả:", response.json())
else:
    print("❌ Predict thất bại!")
    print("Status code:", response.status_code)
    print("Response:", response.text)
