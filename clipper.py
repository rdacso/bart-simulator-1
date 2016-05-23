dublin_to_powell = 6.15
fruitvale_to_union_city = 3.80
orinda_to_richmond = 3.35
hayward_to_concord = 5.20
fremont_to_colma = 6.60 



def load_card(num_one, num_five, num_ten, num_twenty):
	one = num_one * 1
	five = num_five * 5
	ten = num_ten * 10
	twenty = num_twenty * 20
	total_money = one + five + ten + twenty
	return total_money

clipper_card = load_card(2,0,1,0)

def travel_to_destination(fare_price,clipper_card):
	if clipper_card >= fare_price:
		print 'Welcome aboard, enjoy your trip!'
	else:
		print 'You need more money'

print travel_to_destination(fruitvale_to_union_city,clipper_card)