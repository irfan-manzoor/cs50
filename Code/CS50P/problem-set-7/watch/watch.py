import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match the src attribute of an iframe element
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/([^/"]+))".*?>'

    # Search for the pattern in the input HTML string
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the matched URL
        video_id = match.group(2)

        # Convert the URL to the shorter youtu.be format
        youtu_be_url = f"https://youtu.be/{video_id}"

        return youtu_be_url
    else:
        # If no match is found, return None
        return None


if __name__ == "__main__":
    main()
