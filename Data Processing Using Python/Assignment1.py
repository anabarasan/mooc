# Write a program to find the 6-th Monisen number.
#
# Classic Programming Question:
# find the n-th Monisen number.
# A number M is a Monisen number if M=2**P-1 and both M and P are prime numbers.
# For example,
# if P=5, M=2**P-1=31.
# 5 and 31 are both prime numbers.
# so 31 is a Monisen number.

def is_prime(x):
    if x < 2:
        return False
        
    if x == 2 or x == 3:
        return True
        
    if x % 2 == 0:
        return False
        
    for i in range(3,x):
        if x % i == 0:
            return False
    return True


calculate_monisen_number = lambda p: (2 ** p) -1

count = 0
num = 1
while True:
    if is_prime(num):
        monisen_number = calculate_monisen_number(num)
        if is_prime(monisen_number):
            count += 1
            if count == 6:
                print(num, monisen_number)
                break
    num += 1

