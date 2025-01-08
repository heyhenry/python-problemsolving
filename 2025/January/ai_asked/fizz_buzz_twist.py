"""
Problem 2: FizzBuzz with a Twist

Write a function that generates a list of strings for numbers 1 through n. 
For multiples of 3, append "Fizz"; 
for multiples of 5, append "Buzz"; 
for numbers divisible by both, append "FizzBuzz". 
If the number is a prime number, append "Prime" instead.

Constraints:
1 <= n <= 100.
"""
def is_prime(n : int):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fizz_buzz_twist(n : int) -> list[str]:
    results = []
    for i in range(1, n+1):
        if is_prime(i):
            results.append('Prime')
        elif i % 3 == 0 and i % 5 == 0:
            results.append('FizzBuzz')
        elif i % 3 == 0:
            results.append('Fizz')
        elif i % 5 == 0:
            results.append('Buzz')
        else:
            results.append(str(i))
    return results

print(fizz_buzz_twist(15))
# result: 
# [
#     '1', 'Prime', 'Prime', '4', 'Prime', 'Fizz', 'Prime', '8', 'Fizz', 'Buzz', 'Prime', 'Fizz', 'Prime', '14', 'FizzBuzz'
# ]
