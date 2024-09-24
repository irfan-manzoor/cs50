import csv
import sys


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Read database file
    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    with open(database_filename, 'r') as db_file:
        reader = csv.DictReader(db_file)
        data = [row for row in reader]
        str_names = reader.fieldnames[1:]  # Get STR names (exclude the first column 'name')
        individuals = [row['name'] for row in data]

    # Read DNA sequence file
    with open(sequence_filename, 'r') as seq_file:
        sequence = seq_file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_name in str_names:
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check for matching profiles
    for person in data:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_names):
            print(person['name'])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
