def record_rainfall():
	rainfall = {}
	while True:
		city_name = input('輸入城市 : ')
		if not city_name:
			break
		rain_mm = input('請輸入降雨量 : ')
		if not rain_mm :
			rain_mm = 0
		#dict中的get()如果 dict 中沒有該城市名稱，return 0 
		rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
	for city, rain in rainfall.items():
		print(f'{city}:{rain} mm')	    
record_rainfall()

# 使用Python 中 defaultdict 的物件，當你存取一個不存在的 key 時，它會自動幫你建立這個 key，並給一個預設值
# 以下做函式的改寫
from collections import defaultdict
def record_rainfall_with_defaultdict():
	rainfall = defaultdict(int)
	while True:
		if not (city_name:=input('輸入城市 : ')):
			break
		if not (rain_mm:=input('請輸入降雨量 : ')):
			rain_mm = 0
		rainfall[city_name] += int(rain_mm)
	for city, rain in rainfall.items():
		print(f'{city}: {rain} mm')
record_rainfall_with_defaultdict()			




