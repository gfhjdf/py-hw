### 1

def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(2, int((n ** 0.5) // 1) + 1):
            if n % i == 0:
                return False
        
    return True


### 2

def digit_sum(k):
    return sum([int(num) for num in str(k)])

print(digit_sum(24))
### 3

def powering(n):
    num = 2
    counter = 1

    while num < n:
        num = 2 ** counter
        
        if 2 ** counter < n:
            print(2 ** counter)
        counter += 1 
