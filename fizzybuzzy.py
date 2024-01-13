### FizzBuzz is a challenge that involves writing code that labels: 

for num in range(1,101):
    string = ""
## Numbers divisible by three as “Fizz" 
    if num % 3 == 0:
        string = string + "Fizz"

## Numbers divisible by four as “Buzz” 
    if num % 4 == 0:
        string = string + "Buzz"
        
## Numbers divisible by both as “FizzBuzz”
    if num % 4 != 0 and num % 3 != 0:
        string = string + str(num)

    print(string)
