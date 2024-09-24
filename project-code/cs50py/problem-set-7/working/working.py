import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define regular expression patterns for valid time formats
    pattern1 = r'^(\d{1,2}):(\d{2})\s(AM|PM)\s+to\s+(\d{1,2}):(\d{2})\s(AM|PM)$'
    pattern2 = r'^(\d{1,2})\s(AM|PM)\s+to\s+(\d{1,2})\s(AM|PM)$'

    # Check if input string matches either pattern
    match1 = re.match(pattern1, s)
    match2 = re.match(pattern2, s)

    if match1:
        # Extract time components
        hour1, minute1, period1, hour2, minute2, period2 = match1.groups()
    elif match2:
        # Extract time components (assuming default minutes as 00)
        hour1, period1, hour2, period2 = match2.groups()
        minute1 = minute2 = '00'
    else:
        raise ValueError("Invalid input format")

    # Convert time to 24-hour format
    hour1 = int(hour1)
    if period1 == 'PM' and hour1 != 12:
        hour1 += 12
    elif period1 == 'AM' and hour1 == 12:
        hour1 = 0

    hour2 = int(hour2)
    if period2 == 'PM' and hour2 != 12:
        hour2 += 12
    elif period2 == 'AM' and hour2 == 12:
        hour2 = 0

    # Validate the converted hours
    if hour1 > 23 or hour2 > 23 or int(minute1) > 59 or int(minute2) > 59:
        raise ValueError("Invalid time")

    # Return the formatted time
    return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"


if __name__ == "__main__":
    main()
