one = 0
five =0
ten = 0
twenty = 0

def load_card(num_one, num_five, num_ten, num_twenty):
	global one
	one = num_one * 1
	global five
	five = num_five * 5
	global ten
	ten = num_ten * 10
	global twenty
	twenty = num_twenty * 20
	total_money = one + five + ten + twenty
	return total_money

print load_card(3,1,1,3)