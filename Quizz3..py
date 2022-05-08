# #1
# import requests
# req = requests.get('http://www.pythonchallenge.com/')
# print(req.status_code)
# print(req.headers)
# print(req.text)
#
# #2
# import json
# city = 'Gori'
# key = 'b0382a9da8d31051dd5eecdc220673dc'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
# r = requests.get(url)
# print(r.json())
# res = json.dumps(r.json(),indent=4)
# with open('weather_json','w')as json_file:
#     json_file.write(res)
#
# # სხვა გზით :
# # with open('json_file','w')as file:
# #     json.dump(r.json,file,indent=4)
#
# #3
# result = json.loads(r.text)
# temp = result["main"]["temp"]
# temp_feels = result["main"]["feels_like"]
# print("Temperature is :",temp,"Celsius,  but it feels like", temp_feels)

#4
import sqlite3
conn = sqlite3.connect("weather_api_table")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE weather1
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   city varchar(50),
                   celsius FLOAT )''')
city_list = [( 'Tbilisi',10),
     ( 'Gori',7.77),
     ( 'Rustavi',11),
     ( 'Kutaisi',6),
     ( 'Zestaponi',12)]
cursor.executemany('INSERT INTO weather1 (city,celsius) VALUES (?,?)', city_list)
conn.commit()