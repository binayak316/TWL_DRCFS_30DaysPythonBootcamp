# divisible by 3, print Fizz
# divisible by 5 , print Buzz
# divisible by both 3 and 5, FizzBuzz
# if divisible by none , print the number as it is



# 1. for number inut , we use for loop
# 2. 4 conditional statement for checking divisibility


for i in range(1,50):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(f"print {i}")
  