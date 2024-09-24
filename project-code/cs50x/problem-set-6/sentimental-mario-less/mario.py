from cs50 import get_int


def main():
    # Prompt user for the height of the pyramid
    height = 0
    while height < 1 or height > 8:
        height = get_int("Height: ")

    # Print the half-pyramid aligned to the right
    for i in range(1, height + 1):
        # Calculate the number of spaces and hashes for the current row
        spaces = height - i
        hashes = i
        print(" " * spaces + "#" * hashes)


if __name__ == "__main__":
    main()
