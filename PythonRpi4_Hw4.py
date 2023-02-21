import requests #import module
url = 'https://raw.githubusercontent.com/UncleEngineer/RaspberryPi4/main/test-iot.json'
r = requests.get (url) #กำหนดค่าตัวแปล r

r.status_code #ตัวสอบ status url

r.jason() #เรียกค่า Json จากตัวแปล r ตาม url

data = r.json() #กำหนดตัวแปล  data = r.json

print(data['name'])

print(data['temperature'])

