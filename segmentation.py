import os
from pycantonese import segment

def process_file(input_file_path):
    """
    Performs word segmentation on a Cantonese transcription file.

    Args:
        input_file_path (str): Path to the input file.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        return

    # Get the directory and filename from the input file path
    directory, filename = os.path.split(input_file_path)
    output_file_path = os.path.join(directory, f"segmented_{filename}")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        total_lines = len(lines)
        for i, line in enumerate(lines, start=1):
            if line.startswith('*INV:'):
                continue
            elif line.startswith('*SUB:'):
                line = line.replace('*SUB:', '', 1)
                segmented_line = ' '.join(segment(line.strip()))
                output_file.write(segmented_line + '\n')
            else:
                segmented_line = ' '.join(segment(line.strip()))
                output_file.write(segmented_line + '\n')
            print(f"Processing line {i}/{total_lines}", end="\r")

    print(f"\nWord segmentation completed. Results saved in '{output_file_path}'.")

def main():
    """
    Main function to handle file processing.
    """
    input_file_path = "C:\\Users\\bubufafa\\Downloads\\001 Full Transcription (v3)_LW.txt"
    process_file(input_file_path)

if __name__ == "__main__":
    main()