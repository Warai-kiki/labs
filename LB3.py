from enum import Enum
class month (Enum):
	January = 1
	February = 2
	March = 3
	April = 4
	May = 5
	June = 6
	July = 7
	August = 8
	September = 9
	October = 10
	November = 11
	December = 12
class season (Enum):
	Winter = 1
	Spring = 2
	Summer = 3
	Autumn = 4
while True:
	while True:
		try:
			s = month[input('month ')]
			break
		except KeyError or TypeError :
			print('It must be word')
	if s == month.December or s == month.January or s == month.February :
		m = season.Winter.name
		print (m)
	elif s == month.March or s == month.April or s == month.May :
		m = season.Spring.name
		print(m)
	elif s == month.June or s == month.July or s == month.August :
		m = season.Summer.name
		print (m)
	else:
		m = season.Autumn.name
		print(m)
	print('Would you try again? Write yes or no')
	l = input('')
	if l == 'yes':
		continue
	else:
		break