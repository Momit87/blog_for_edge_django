
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking input from the user
n = int(input("Enter the number of elements: "))

user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

#printing the prime numbers


print("Prime numbers are :",end=" ")
for i in range(0,n):
    if(is_prime(numbers[i])):
        print(numbers[i],end=" ")
    
