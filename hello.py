day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2

print(day2)
# ('thursday', 'friday', 'saturday', 'sunday', ('monday', 'tuesday', 'wednesday'))

print(day2[4][0]) # monday