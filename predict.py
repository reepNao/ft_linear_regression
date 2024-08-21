import json
import sys

def get_thetas() :
	try:
		with open("thetas.json", "r") as read_file:
			data = json.load(read_file)
	except:
		sys.exit(-1)
	return data["theta0"], data["theta1"]

def price_prediction() :
	theta0, theta1 = get_thetas()
	while(1):
		s = input("What is the mileage of your car? (in km): ")
		if not s:
			print('Enter a mileage')
		else:
			break
	try:
		assert(all([c in '-0123456789' for c in s]))
	except:
		print('Use only numbers and "-"')
		sys.exit(-1)
	km_input = float(s)
	if km_input < 0:
		print("A mileage can not be under 0")
		sys.exit(-1)
	if km_input >= 240000:
		print("Your mileage is too high, we can not estimate the price of your car.")
		sys.exit(-1)
	km = (km_input - 22899) / (240000 - 22899)
	price = theta0 + km * theta1
	print("Your prediction price about " + str(int(price)))


if __name__ == '__main__' :
	price_prediction()