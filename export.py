import os
import math

def split_csv(input_file, output_dir, num_segments, n):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the input file and count the number of lines
    with open(input_file, 'r') as f:
        lines = f.readlines()
        total_lines = len(lines)

    # Calculate the number of lines per segment
    lines_per_segment = math.ceil(total_lines / num_segments)

    # Iterate over each segment
    for i in range(num_segments):
        # Calculate the start and end indices for the current segment
        start_idx = i * lines_per_segment
        end_idx = min((i + 1) * lines_per_segment, total_lines)

        # Extract lines for the current segment
        segment_lines = lines[start_idx:end_idx:n]  # Save every Nth line

        # Write segment to file
        segment_output_file = os.path.join(output_dir, f'segment_{i + 1}.csv')
        with open(segment_output_file, 'w') as f_out:
            f_out.writelines(segment_lines)

# Example usage:
input_file = './Projekt/LTSpice/Digital/iout.txt'  # Replace 'input.csv' with your input file name
output_dir = './Projekt/LTSpice/Digital/traces/iout/'    # Replace 'segments' with your desired output directory name
num_segments = 2            # Number of segments to split the file into
n = 500                      # Save every Nth line
split_csv(input_file, output_dir, num_segments, n)