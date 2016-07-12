#Created on 7/5/16 by cwklausing to fool around in python
connor = "connor"
print "this is connor: " + connor
print "this is connor*3: " + connor*3
print "this is connor[2]:" + connor[2]
print "A {} is a type of {}".format("cat", "animal")
#Okay, so can I use variables instead of strings in format?
string1 = 'cat'
string2 = 'animal'
print "A {} is a type of {}".format(string1, string2);#Yes, apparently we can!

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

#Checking out cool slicing available in python
numberLi = [1, 2, 3, 4, 5, 6, 7, 8]
#numbers between index 1 and 4
print numberLi[1:4]
#numbers before index 3
print numberLi[:3]
#numbers after index 3
print numberLi[3:]
#prints every third number in the list
print numberLi[::3]

#now adding another list to numberLi
numberLi2 = [8, 9, 10, 11]
numberLi.extend(numberLi2)
print numberLi
#whoops! We added 8 twice! Let's delete the first '8'
del numberLi[7]
#much better!
print numberLi
#Check for existence of 8 in numberLi
print 8 in numberLi
#Does python type coerce strings to numbers?
print "8" in numberLi #No, apparently not
#Tried to remove all the even numbers from the array
    # evens = numberLi[::2]
    # numberLi.remove(evens)
    #But apparently this doesn't work--can only remove one
    #value from the list at a time.
#Instead, try removing them manually:
numberLi.remove(2)
numberLi.remove(4)
numberLi.remove(6)
numberLi.remove(8)
numberLi.remove(10)
print numberLi
