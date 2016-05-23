
def load_card(num_one, num_five, num_ten, num_twenty):
	one = num_one * 1
	five = num_five * 5
	ten = num_ten * 10
	twenty = num_twenty * 20
	total_money = one + five + ten + twenty
	return total_money

print load_card(3,1,1,3)