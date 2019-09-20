#!/usr/bin/env python

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
hundreds = {100: 'onehundredand', 200: 'twohundredand', 300: 'threehundredand', 400: 'fourhundredand', 500: 'fivehundredand', 600: 'sixhundredand', 700: 'sevenhundredand', 800: 'eighthundredand', 900:'ninehundredand'}

def get_string(n):
	s = ''
	t = str(n)
	if len(t) == 1:
		s = ones[int(t[0])]
	elif len(t) == 2:
		if t[1] == '0':
			s = tens[int(t[0] + '0')]
		elif t[0] == '1' and t[1] != '0':
			s = teens[int('1' + t[1])]
		else:
			if t[1] == '0':
				s = tens[int(t[0] + '0')]
			else:
				s = tens[int(t[0] + '0')] + ones[int(t[1])]
	elif len(t) == 3:
		if t[1] == '0' and t[2] == '0':
			s = hundreds[int(t[0] + '0' + '0')][:-3]
		elif t[1] == '0' and t[2] != '0':
			s = hundreds[int(t[0] + '0' + '0')] + ones[int(t[2])]
		elif t[1] == '1' and t[2] == '0':
			s = hundreds[int(t[0] + '0' + '0')]	+ tens[10]
		elif t[1] == '1' and t[2] != '0':
			s = hundreds[int(t[0] + '0' + '0')]	+ teens[int(t[1] + t[2])]
		else:
			if t[2] == '0':
				s = hundreds[int(t[0] + '0' + '0')]	+ tens[int(t[1] + '0')]
			else:
				s = hundreds[int(t[0] + '0' + '0')]	+ tens[int(t[1] + '0')] + ones[int(t[2])]
	return s

total = 0
for i in range(1, 1000):
	total += len(get_string(i))
print(total + 11) # len(onethousand) = 11