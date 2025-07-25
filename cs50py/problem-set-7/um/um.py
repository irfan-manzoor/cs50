import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Using regular expression to find all occurrences of "um" as a whole word
    um_count = len(re.findall(r'\bum\b', s, re.IGNORECASE))
    return um_count


if __name__ == "__main__":
    main()
