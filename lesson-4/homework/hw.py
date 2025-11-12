### 1

color_dict = {
    "primary_1": "Red",
    "primary_2": "Blue",
    "primary_3": "Yellow",
    "secondary_1": "Green",
    "secondary_2": "Purple"
}

asc_order = dict(sorted(color_dict.items(), key=lambda kv: kv[1]))
desc_order = dict(sorted(color_dict.items(), key=lambda kv: kv[1], reverse=True))

print(asc_order)
print("\n")
print(desc_order)
### 2

nums = {
    0: 10,
    1: 20
}

nums[2] = 30
print(nums)
### 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

main = dic1.copy() | dic2.copy() | dic3.copy()
print(main)

### 4

n = int(input())
nums = {}

for i in range(1, n + 1):
    nums[i] = i * i

print(nums)
### 5

nums = {}

for i in range(1, 16):
    nums[i] = i * i

print(nums)

### SET EXERCISES

### 1

sample_set = set()

### 2

color_set = {"Red", "Blue", "Green", "Yellow", "Purple", "Red", "Blue"}

for i in color_set:
    print(i)


### 3

members = {"Alex", "Bella", "Charlie", "David", "Alex", "Ethan", "Bella"}
members.add(input())

print(members)
### 4

members = {"Alex", "Bella", "Charlie", "David", "Alex", "Ethan", "Bella"}

members.discard("Alex")
members.discard("Alex")
print(members)
### 5

members = {"Alex", "Bella", "Charlie", "David", "Alex", "Ethan", "Bella"}

members.discard("Alex")
print(members)

