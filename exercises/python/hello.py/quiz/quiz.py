import csv
from sys import argv
import random
import math

script, questions, topic, difficulty = argv

csv_file = open("quiz.csv")
csv_reader = csv.reader(csv_file)

quest = []
quest2= []
for question in csv_reader:
    if question[1] == topic and question[2] <= difficulty:
        quest.append(question)
    else:
        quest2.append(question)


min, max = 0, 20
new_rand = min + (random.random() * (max-min))
add = math.floor(new_rand)
add1 = int(add)

while len(quest) != 10:
    next_one = quest2.pop(add1)
    quest.append(next_one)

print quest






