x = 10

try:
    result = x / 2
except ZeroDivisionError:
    print("You can't divide by zero lah!")
else:
    print("Division succesful. Result:", result)
finally:
    print("This will always run")