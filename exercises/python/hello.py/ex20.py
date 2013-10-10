from sys import argv # importing argument variable from system

script, input_file = argv #setting 2 variables = to the argv

def print_all(f): #setting a function call print_all with f as the parameter
    print f.read() #printing out the functions read which reads the f variable

def rewind(f): #setting a method called rewind with the f parameter
    f.seek(0) #setting the f parameter to the seek function to the first line

def print_a_line(line_count, f): #defining a function with the parameters of line_count and f
    print line_count, f.readline() #printing out the line count and f with the function of readline

current_file = open(input_file) # setting a variable to the open functions

print "First let's print the whole file:\n"

print_all(current_file) #calling the print_all function with the current_file parameter

print "Now let's rewind, kind of like a tape."

rewind(current_file) #calling the rewind function with the current_file parameter

print "Let's print three lines:"

current_line = 1 #setting the current line
print_a_line(current_line, current_file)#calling the print_a_line function with current_line and current_file as the parameters

current_line += 1 #resetting the variable to make it the next line
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

rewind(current_file)

current_line -= 1
print_a_line(current_line, current_file)

current_line -= 1
print_a_line(current_line, current_file)
