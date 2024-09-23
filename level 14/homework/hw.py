num1 =(input("enter your first num: "))
num2 =(input("enter your second num: "))

print ("operator")
print("+,-,/,*")
operator = (input("enter your operator: "))

if operator == "+":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1) - int(num2))
elif operator == "/":
    print(int(num1) / int(num2))
elif operator == "*":
    print(int(num1) * int(num2))
    if num1 or num2 == 0:
        print("you cant use 0 in our calculator")