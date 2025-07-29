1
def is_prime(n):
    if n <= 1:  
        print(False)
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(False)
            return
    print(True)


2
def digit_sum(k):
    s = 0
    while k>0:
        s+= k%10
        k//=10
    print(s)


3
def print_powers_of_two(n):
    s = 1
    numbers = []
    while 2**s<=n:
        numbers.append(str(2**s))
        s+=1
    print(" ".join(numbers))
