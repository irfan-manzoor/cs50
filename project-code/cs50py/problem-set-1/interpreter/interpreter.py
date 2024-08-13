def main():
    expression = input("Expression: ")
    equation(expression)

def equation(x):
    x,y,z = x.split(" ")
    x2 = float(x)
    z2 = float(z)

    if y == "+":
        result = x2 + z2
    elif y == "-":
        result = x2 - z2
    elif y == "*":
        result = x2 * z2
    elif y == "/":
        result = x2 / z2

    print(f"{result:.1f}")

main()
