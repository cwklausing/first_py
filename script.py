#Created on 7/5/16 by cwklausing to fool around in python
connor = "connor"
print "this is connor: " + connor
print "this is connor*3: " + connor*3
print "this is connor[2]:" + connor[2]

print "A {} is a type of {}".format("cat", "animal")

#Okay, so can I use variables instead of strings in format?

string1 = 'cat'
string2 = 'animal'

print "A {} is a type of {}".format(string1, string2);
#Yes, apparently we can!

#working with division and decimals

regDivision = 8 / 3
# Tried this: print "this is regular division: " + regDivision
# and it doesn't work, since you apparently can't concatonate str and int values
#Instead, use the above string format:
print "This is regular division: {}".format(regDivision)
decimalDivision = 8.0 / 3.0
print "this is decimal division: {}".format(decimalDivision)

#using ternary in python
print "hello" if 4 < 3 else "goodbye"
print "hello" if 3 < 4 else "goodbye"

#Lists!
sandwichLi = []
sandwichLi.append("PB&J")
sandwichLi.append("Reuben")
sandwichLi.append("BLT")
print sandwichLi

#remove BLT using the pop() method
blt = sandwichLi.pop()
print sandwichLi
#Now reappend it
sandwichLi.append(blt)
print sandwichLi
