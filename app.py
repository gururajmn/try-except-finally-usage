a= 5
b=2

try:
    print('resource opened')
    print(a/b)
    k=int(input("Enthe the number: "))
    print(k)

except ZeroDivisionError as e:
    print("the number is not divisible by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("something went wrong!!!!")

finally:
    print('resource closed')