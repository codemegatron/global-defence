aliens = 2
password = "ONE VISION"

print("ALIENS ARE INVADING THE PLANET")
print("WE NEED THE PASSWORD")
print()
print("----------------------------------------------------")
print("               GLOBAL DEFENCE NETWORK               ")
print("----------------------------------------------------")
print()

passwordguess = input("PASSWORD--> ").upper()
 
while passwordguess != password:
	print()
	print("INCORRECT PASSWORD")
	print()
	aliens = aliens ** 12
	print("NOW THERE ARE", aliens, "ALIENS. TRY AGAIN")
	if aliens > 7400000000:
		break
	print()
	passwordguess = input("INPUT PASSWORD-->").upper()
if aliens > 7400000000:
	print("ALIENS HAVE OUTNUMBERED US.")
else:
	print("WE DEFEATED THE ALIENS WITH OUR NEUTRON BOMB.")
