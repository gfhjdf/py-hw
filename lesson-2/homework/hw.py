### 1

name = input("Enter your name: ")
y_of_birth = int(input("Enter the year of your birth: "))

print(f"{name}, your age is {2025 - y_of_birth}.")
### 2
#      0123456789       
txt = 'LMaasleitbtui'

print(txt[0] + txt[3:5] + txt[6] + txt[8] + txt[10] + txt[-1])
print(txt[1:3] + txt[5] + txt[7] + txt[9] + txt[11])
### 3
#      0123456789
txt = 'MsaatmiazD'

print(txt[-1] + txt[2] + txt[5] + txt[7] + txt[1])
print(txt[0] + txt[3:5] + txt[6] + txt[8])
### 4

txt = "I'am John. I am from London"

print(txt[21:])

### 5

text = input()

print(text[::-1])
### 6

text = input()

print(text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u") + text.count("y"))
### 7

nums = input().split(", ")

print(max(nums))
### 8

word = input()

if word == word[::-1]:
    print("the word is a palindrome")
else:
    print("the word isn't a palindrome")
### 9

email = input()

print(email[email.find("@"):])
### 10

import secrets

print(secrets.token_urlsafe(8))
