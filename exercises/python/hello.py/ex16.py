from sys import argv

script, filename = argv

print "We're going to erase %r" %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,"w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to write these to the file"

target.write("I'm learning \nthis stuff\nWish I had more time.")

print "And finally, we close it."
target.close()