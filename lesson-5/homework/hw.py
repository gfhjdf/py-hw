### 1

def is_leap(year) -> bool:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
### 2
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

### 3

### 3.1 -> first solution with if
a = int(input())
b = int(input())
nums = list(range(a, b + 1))
even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)

### 3.2 -> second solution without if
# honestly, couldnt find a solution which doesn't use "if". give me a full code and explain me each line.






