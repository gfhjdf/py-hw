### 1


### 2

n = int(input())

for num in range(0, n):
    print(num ** 2)

### 3

nums = []
counter = 1
while counter <= 10:
    nums.append(counter)
    print(*nums)

    counter += 1
### 3.2

n = int(input())
result = 0

for num in range(1, n + 1):
    result += num

print(result)

### 4

num = int(input())

for i in range(1, 11):
    print(num * i)
### 5
# couldn't get the meaning of the task. so left undone.
numbers = [12, 75, 150, 180, 145, 525, 50]


### 6

number = 75869

print(len(str(number)))
### 7

nums = [5, 4, 3, 2, 1]

for i in range(len(nums)):
    print(*nums)
    nums.pop(0)


### 8

list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
    print(i)
### 9

for i in range(-10, 0):
    print(i)
### 10

for i in range(0, 5):
    print(i)

print("Done!")
### 11

for i in range(25, 51):
    flag = True

    if i % 2 == 0:
        continue
    else:
        for j in range(2, int((i ** 0.5) // 1) + 1):
            if i % j == 0:
                flag = False
                break

    
    if flag:
        print(i)
### 12
fibo = [0, 1]
num, fib = 0, 1

for i in range(8):
    num, fib = fib, num + fib

    fibo.append(fib)


print(*fibo)  


### 13

given_num = 5
result = 1

for i in range(1, given_num + 1):
    result *= i

print(result)
### 4. -> return uncommon elements of lists task
# ig the code works well. all you need to do is just replace the values for both lists.
 
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

main_ls = []

for i in list1:
    if i not in list2:
        main_ls.append(i)

for j in list2:
    if j not in list1:
        main_ls.append(j)

print(main_ls)


