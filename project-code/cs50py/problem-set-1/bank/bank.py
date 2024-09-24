def main ():
    # ask user for greeting
    greet = input("Greeting: ")
    greeting(greet)

def greeting(greet):
    greeting = greet.strip().lower()

    if "hello" in greeting:
        print("$0")
    elif greeting.startswith("h") and greeting != "hello":
        print("$20")
    else:
        print("$100")

main()
