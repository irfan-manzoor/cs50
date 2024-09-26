import sys
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)

def main():
    figlet = Figlet()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # Output text in a random font
        user_text = input("Enter text: ")
        print(figlet.renderText(user_text))
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Output text in a specific font
        font_name = sys.argv[2]
        if font_name not in figlet.getFonts():
            print("Invalid font name")
            sys.exit(1)
        else:
            user_text = input("Enter text: ")
            figlet.setFont(font=font_name)
            print(figlet.renderText(user_text))
    else:
        print_usage_and_exit()

if __name__ == "__main__":
    main()
