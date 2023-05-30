c = int(0)
s = 0
x = 0
y = 0
z = float(0)

print('''.......................................
*** Welcome to M.O. Calculator ***
---------------------------------------
$$ Choose Operator You Need...

Arithmetic Operators
> 1 = Addition (+)
> 2 = Subtraction (-)
> 3 = Multiplication (*)
> 4 = Division (/)
> 5 = Modulus (%)
> 6 = Exponent (**)
> 7 = Floor Division (//)

Assignment Operators
> 8 = Addition Assignment (+=)
> 9 = Subtraction Assignment (-=)
> 10 = Multiplication Assignment (*=)
> 11 = Division Assignment (/=)
> 12 = Remainder Assignment (%=)
> 13 = Exponent Assignment (**=)
> 14 = Floor Division Assignment (//=)

Bitwise Operators
> 15 = Binary AND (&)
> 16 = Binary OR (|)
> 17 = Binary XOR (^)
> 18 = Binary NOT / Binary Ones Complement (~)
> 19 = Binary Left Shift (<<)
> 20 = Binary Right Shift (>>)

Comparison Operators
> 21 = Equal (==)
> 22 = Not Equal (!=)
> 23 = Greater Than (>)
> 24 = Less Than (<)
> 25 = Greater than or Equal to (>=)
> 26 = Less than or Equal to (<=)
.......................................''')

c = int(input("Operator You Need :- "))
if c == 1:
    print("Operator Addition (+)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x + y
    print(x, "+", y, "=", z)
elif c == 2:
    print("Operator Subtraction (-)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x - y
    print(x, "-", y, "=", z)
elif c == 3:
    print("Operator Multiplication (*)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x * y
    print(x, "*", y, "=", z)
elif c == 4:
    print("Operator Division (/)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x / y
    print(x, "/", y, "=", z)
elif c == 5:
    print("Operator Modulus (%)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x % y
    print(x, "%", y, "=", z)
elif c == 6:
    print("Operator Exponent (**)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x ** y
    print(x, "**", y, "=", z)
elif c == 7:
    print("Operator Floor Division (//)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x // y
    print(x, "//", y, "=", z)
elif c == 8:
    print("Operator Addition Assignment (+=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x += y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 9:
    print("Operator Subtraction Assignment (-=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x -= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 10:
    print("Operator Multiplication Assignment (*=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x *= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 11:
    print("Operator Division Assignment (/=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x /= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 12:
    print("Operator Remainder Assignment (%=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x %= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 13:
    print("Operator Exponent Assignment (**=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x **= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 14:
    print("Operator Floor Division Assignment (//=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    s = int(input("Number of Loops required for Your Operator :- "))
    for z in range(s):
        x //= y
        print("Loop no.", z, "---", "x =", x, "|", "y =", y)
elif c == 15:
    print("Operator Binary AND (&)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x & y
    print(x, "&", y, "=", z)
elif c == 16:
    print("Operator Binary OR (|)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x | y
    print(x, "|", y, "=", z)
elif c == 17:
    print("Operator Binary XOR (^)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x ^ y
    print(x, "^", y, "=", z)
elif c == 18:
    print("Operator Binary NOT / Binary Ones Complement (~)")
    print(".......................................")
    x = int(input("First Number :- "))
    z = ~x
    print("~", x, "=", z)
elif c == 19:
    print("Operator Binary Left Shift (<<)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x << y
    print(x, "<<", y, "=", z)
elif c == 20:
    print("Operator Binary Right Shift (>>)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x >> y
    print(x, ">>", y, "=", z)
elif c == 21:
    print("Operator Equal (==)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x == y
    print(x, "==", y, "---", z)
elif c == 22:
    print("Operator Not Equal (!=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x != y
    print(x, "!=", y, "---", z)
elif c == 23:
    print("Operator Greater Than (>)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x > y
    print(x, ">", y, "---", z)
elif c == 24:
    print("Operator Less Than (<)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x < y
    print(x, "<", y, "---", z)
elif c == 25:
    print("Operator Greater than or Equal to (>=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x >= y
    print(x, ">=", y, "---", z)
elif c == 26:
    print("Operator Less than or Equal to (<=)")
    print(".......................................")
    x = int(input("First Number :- "))
    y = int(input("Second Number :- "))
    z = x <= y
    print(x, "<=", y, "---", z)
else:
    print('Invalid Operator Number')
    print(".......................................")
