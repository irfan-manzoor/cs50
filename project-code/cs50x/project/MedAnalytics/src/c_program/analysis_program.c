#include <stdio.h>   // For standard input/output functions
#include <stdlib.h>  // For standard library functions (e.g., memory allocation, exit)
#include <string.h>  // For string handling functions (e.g., strcmp)

// Function to detect anomalies in health data (heart rate, blood glucose, temperature, and blood pressure)
void detect_anomalies(float heart_rate, float glucose, float temp, const char* bp) {
    // Check if heart rate is outside the normal range (60-100 bpm)
    if (heart_rate < 60 || heart_rate > 100) {
        printf("Abnormal heart rate: %.2f bpm\n", heart_rate);
    }
    // Check if blood glucose is outside the normal range (70-140 mg/dL)
    if (glucose < 70 || glucose > 140) {
        printf("Abnormal blood glucose: %.2f mg/dL\n", glucose);
    }
    // Check if temperature is outside the normal range (36.1-37.2°C)
    if (temp < 36.1 || temp > 37.2) {
        printf("Abnormal temperature: %.2f°C\n", temp);
    }
    // Check if blood pressure is not equal to "120/80"
    if (strcmp(bp, "120/80") != 0) {
        printf("Abnormal blood pressure: %s\n", bp);
    }
}

int main(int argc, char *argv[]) {
    // Check if the program has received at least one argument (the CSV file path)
    if (argc < 2) {
        // Print usage message if no file path is provided
        fprintf(stderr, "Usage: %s <csv file>\n", argv[0]);
        return 1;  // Exit with error code 1
    }

    // Open the CSV file in read mode
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        // If the file cannot be opened, print an error message and exit
        perror("Error opening file");
        return 1;  // Exit with error code 1
    }

    char line[1024];  // Buffer to hold each line of the CSV file

    // Read and skip the first line (header of the CSV file)
    fgets(line, sizeof(line), file);

    // Read each subsequent line in the CSV file
    while (fgets(line, sizeof(line), file)) {
        float heart_rate, glucose, temp;  // Variables to hold health data
        char bp[16];  // Variable to hold blood pressure (as a string)

        // Parse the line from the CSV file to extract heart rate, glucose, temperature, and blood pressure
        // %*d skips the first integer column (assuming it’s a timestamp or ID)
        sscanf(line, "%*d,%f,%f,%f,%s", &heart_rate, &glucose, &temp, bp);

        // Call the function to detect anomalies based on the extracted data
        detect_anomalies(heart_rate, glucose, temp, bp);
    }

    // Close the file after processing is complete
    fclose(file);
    return 0;  // Exit with success code 0
}
