clear()
want_to_have = 500000
tilled = False
while not got_want_to_have(want_to_have):
	tilled = farm(want_to_have,tilled)