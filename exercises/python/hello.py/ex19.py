def cheese_and_crackers(cheese_count, boxes_of_cracker): # setting a function
    print "You have %d cheeses!" % cheese_count #printing cheese count
    print "You have %d boxes of crackers" % boxes_of_cracker #printing cracker count
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30) # giving the function values

print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_crackers + 100, amount_of_crackers + 1000)

def chicken_and_waffles(chicken, waffles):
    print "I would like %d waffles" % waffles
    print "I would like %d pieces of chicken" % chicken

chicken_and_waffles(amount_of_crackers - 10, amount_of_cheese + 20)