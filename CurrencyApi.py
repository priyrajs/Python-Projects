import requests



def currencies():
	url = 'https://api.currencyfreaks.com/v2.0/currency-symbols'
	response_API = requests.get(url)
	# print(response_API.status_code)
	if response_API.status_code == 200:
		json_val = response_API.json()
		currencies = json_val['currencySymbols']
		# print(currencies)
		return currencies
		# print(currencies)


# def currencies():
# 	key = 'bc296ce1e30642ef9546b1c8701a6799'
# 	url = f'https://api.currencyfreaks.com/latest?apikey={key}'
# 	response_API = requests.get(url)
# 	# print(response_API.status_code)
# 	if response_API.status_code == 200:
# 		json_val = response_API.json()
# 		# print(json_val)
# 		currencies = sorted(json_val['rates'].keys())
# 		# print(currencies)
# 		return currencies
# 		# print(currencies)

def rateof(country="INR"):
	# print(country,'cool')
	dict1 = {}
	key = 'bc296ce1e30642ef9546b1c8701a6799'
	url = f'https://api.currencyfreaks.com/latest?apikey={key}'
	response_API = requests.get(url)
	# print(response_API.status_code)
	if response_API.status_code == 200:
		json_val = response_API.json()
		ind_rate = float(json_val['rates']['INR'])
		req_rate = float(json_val['rates'][country])
		dict1['ind_rate'] = ind_rate
		dict1['req_rate'] = req_rate
		return dict1
		# print(dict1)

# currencies2()

# def render():
# 	dict1 = []
# 	fullname = currencies2()
# 	for i,v in fullname.items():
# 		dict1.append(i+" - "+v)
# 	print(dict1)
# 	# print(type(fullname[0]))
# render()
