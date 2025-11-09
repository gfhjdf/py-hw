### 1

fruits = ['apple', 'banana', 'melon', 'watermelon', 'peach']
print(fruits[2])

### 2

first_ls = [1, 2, 3]
second_ls = [4, 5, 6]

main_ls = first_ls + second_ls
print(main_ls)
### 3

nums = input().split(", ")
print(nums)
new_ls = [nums[0], nums[int(len(nums) / 2)], nums[-1]]

print(new_ls)

### 4

movies = ["Inception", "Interstellar", "inglourious basterds", "Parasite", "Spirited Away"]

new_movies = tuple(movies)

### 5

cities = input().split(", ")

if "Paris" in cities:
    print("Paris is in the list of cities.")
else:
    print("There is no Paris in the list of cities.")
### 6

nums = [3, 7, 1, 9, 4, 6, 8, 2, 5]
nums += nums

print(nums)
### 7

nums = [3, 7, 1, 9, 4, 6, 8, 2, 5]


nums.insert(0, nums[-1])
nums.insert(-1, nums[1])
nums.pop(1)
nums.pop(-1)
print(nums)

#### 8

nums_tuple = (1, 4, 7, 2, 9, 5, 3, 8, 6, 0)
nums_ls = list(nums_tuple)

print(nums_ls[3:7])

### 9

colors = ["blue", "red", "blue", "green", "yellow", "blue", "purple", "orange", "blue", "pink"]

print(colors.count("blue"))
### 10

animals = ("tiger", "elephant", "lion", "giraffe", "zebra", "monkey", "bear")

animals.index("lion")

### 11

t1 = (1, 2, 3)
t2 = (4, 5, 6)

main = t1 + t2

print(main)

### 12
colors = ["blue", "red", "blue", "green", "yellow", "blue", "purple", "orange", "blue", "pink"]
animals = ("tiger", "elephant", "lion", "giraffe", "zebra", "monkey", "bear")

print(len(colors))
print(len(animals))
### 13

nums = (7, 2, 9, 4, 6)
nums_ls = list(nums)


### 14

nums = (7, 2, 9, 4, 6)

print(f"Max:", max(nums))
print(f"Min:", min(nums))
### 15

words = ("apple", "river", "mountain", "computer", "freedom")
words_ls = list(words)
words_ls.reverse()
words = tuple(words_ls)
print(words)

