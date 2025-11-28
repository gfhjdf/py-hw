### 1

try:
    print(7/0)
except ZeroDivisionError:
    print("division by zero. please, try again.")

### 2

try:
    num = int(input("Please, enter a number: "))
except ValueError:
    print("this wasn't a number, please, try again.")


### 3

try:
    with open("file.txt"):
        pass
except FileNotFoundError:
    print("the file wasn't found. please, try again.")
### 4

number = [num.isnumeric() for num in input("Please, enter two numbers: ").strip().split()]

if all(number):
    pass
else:
    raise TypeError("not all objects are numbers. please, try again.")
### 5

try:
    with open("file.txt", "w"):
        pass
except PermissionError:
    print("You don't have access to change this file.")


### 6

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 11):
    try:
        print(ls[i])
    except IndexError:
        print("The code has been stopped due to index error.")
        break


### 7

try:
    num = int(input())
except KeyboardInterrupt:
    print("the process has been stopped.")


### 8

try:
    print(8/0)
except ZeroDivisionError:
    print("An arithmetic error has occurred.")
### 9

try:
    with open("file.txt", "r"):
        pass
except UnicodeDecodeError:
    print("there is an encoding issue. please, try again.")


### 10

num = 2
try:
    num.append(5)
except AttributeError:
    print("something is wrong with your code. attribute error has occurred.")
# Python File Input Output: Exercises, Practice, Solution
### 1

with open("file.txt", "r"):
    pass

### 2

with open("file.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, 5):
        print(lines[i].strip())
### 3

text = "ty"

with open("file.txt", "a") as f:
    f.write(f"\n{text}")
    print(text)
    
### 4

with open("file.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines) - 1, 5, -1):
        print(lines[i].strip())
### 5
with open("file.txt", "r") as f:
    lines = f.readlines()

### 6
with open("file.txt", "r") as f:
    lines = f.read()


### 7
with open("file.txt", "r") as f:
    lines = f.readlines()
    

### 8

def find_longest_word(ls: list):
    len_of_words = {word: len(word) for word in ls}
    sorted_ls = sorted(len_of_words.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_ls[0][0]


with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print(find_longest_word(lines))




### 9

with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    print(len(lines))
### 10

with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    out = {line: lines.count(line) for line in lines}
    
print(out)

### 11

import os

path = "file.txt"
size = os.path.getsize(path)
print(size, "bytes")
### 12
ls = [1, 2, 3]

with open("file.txt", "a") as f:
    for line in ls:
        f.write(f"\n{line}")
### 13

with open("file.txt", "r") as f1, open("file1.txt", "a") as f2:
    lines_F1 = f1.readlines()
    for line in lines_F1:
        f2.write(line)


### 14

with open("main.txt", "w") as f, open("file.txt", "r") as f1, open("file1.txt", "r") as f2:
    lines_F1 = f1.readlines()
    lines_F2 = f2.readlines()
    
    for i in range(0, min([len(lines_F1), len(lines_F2)])):
        f.write(f"{lines_F1[i].strip()} | {lines_F2[i].strip()}\n")
    

### 15
from random import randint

with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    print(lines[randint(0, len(lines))])
### 16

f = open("file.txt", "r")
if f.closed:
    print("closed")
else:
    print("not closed")

f.close()
### 17
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# the objects in the list lines are without "\n"

### 18

filename = input()

with open(filename, "r") as f:
    text = f.read()

words = text.split()

print(len(words))
### 20

letters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

for letter in letters:
    with open(f"{letter}.txt", "w")

### 21
n_of_ch = int(input())
letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0, 27, n_of_ch):
    print(letters[i:i + n_of_ch])
