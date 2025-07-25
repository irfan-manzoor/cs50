#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Define a BYTE type
typedef uint8_t BYTE;

// Define block size
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s forensic_image\n", argv[0]);
        return 1;
    }

    // Remember filenames
    char *input_file = argv[1];

    // Open input file
    FILE *inptr = fopen(input_file, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", input_file);
        return 1;
    }

    // Variables for file writing
    FILE *outptr = NULL;
    char filename[8];
    int file_count = 0;
    BYTE buffer[BLOCK_SIZE];
    int is_writing = 0;

    // Read the forensic image block by block
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, inptr) == BLOCK_SIZE)
    {
        // Check for JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // If already writing a JPEG, close the current file
            if (is_writing)
            {
                fclose(outptr);
            }
            else
            {
                is_writing = 1;
            }

            // Create a new JPEG file
            sprintf(filename, "%03d.jpg", file_count);
            outptr = fopen(filename, "w");
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 1;
            }

            // Increment file count
            file_count++;
        }

        // If currently writing a JPEG, write the block to the file
        if (is_writing)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
        }
    }

    // Close the last JPEG file
    if (is_writing)
    {
        fclose(outptr);
    }

    // Close the input file
    fclose(inptr);

    return 0;
}
