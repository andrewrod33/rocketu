from sys import argv # This imports an argument variable

script, filename = argv # This is setting 2 arguments to the argument variable

txt = open(filename) # this line is calling a function with the parameters of the filename variable

print "Here's your file %r: " %filename # this is just printing the % raw variable filename
print txt.read() #this calls the function

print "Type the filename again:" #printing a string
file_again = raw_input("> ") #setting a variable called file again that 's prompting raw input with the > symbol inside of it

txt_again = open(file_again) #  setting a variable for opening a file again

print txt_again.read() # printing the variable txt_again using the .read() method

