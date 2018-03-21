num1 = input("Enter first number: ");
if num1 == 'x':
    exit();
else:
    num2 = input("Enter second number: ");
    number1 = int(num1);
    number2 = int(num2);
    swap = number1;
    number1 = number2;
    number2 = swap;
    print number1,number2
