import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    evidence = []
    labels = []

    # Define a mapping for month names to their corresponding indices
    month_mapping = {
        'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5,
        'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
    }

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            # Convert month to its corresponding index
            month_index = month_mapping[row[10]]

            # Convert VisitorType to 1 for returning, 0 for non-returning visitors
            visitor_type = 1 if row[15] == 'Returning_Visitor' else 0

            # Convert Weekend to 1 if true, 0 if false
            weekend = 1 if row[16] == 'TRUE' else 0

            # Convert Revenue to 1 if true, 0 if false
            label = 1 if row[-1] == 'TRUE' else 0

            # Append evidence list and label
            evidence.append([
                int(row[0]), float(row[1]), int(row[2]), float(row[3]),
                int(row[4]), float(row[5]), float(row[6]), float(row[7]),
                float(row[8]), float(row[9]), month_index, int(row[11]),
                int(row[12]), int(row[13]), int(row[14]), visitor_type, weekend
            ])
            labels.append(label)

    return evidence, labels


def train_model(evidence, labels):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    # Calculate true positive rate (sensitivity)
    true_positives = sum((l == 1 and p == 1) for l, p in zip(labels, predictions))
    sensitivity = true_positives / sum(labels)

    # Calculate true negative rate (specificity)
    true_negatives = sum((l == 0 and p == 0) for l, p in zip(labels, predictions))
    specificity = true_negatives / (len(labels) - sum(labels))

    return sensitivity, specificity


if __name__ == "__main__":
    main()
