import csv

# Function to convert values like "0.00k" or "1.3m" to numeric values
# Function to convert values like "0.00k" or "1.3m" to numeric values
def convert_value(value):
    value = value.lower()  # Convert the value to lowercase
    if value.endswith('k'):
        return float(value.replace('k', '')) * 1000
    elif value.endswith('m'):
        return float(value.replace('m', '')) * 1000000
    elif value.endswith('b'):
        return float(value.replace('b', '')) *1000000000
    else:
        return float(value)


# Input and output file names
input_file = 'refined.csv'
output_file = 'newrefined.csv'

# Open the input CSV file
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # Read the header row

    # Read and process each row in the input file
    rows = []
    for row in reader:
        row[0] = convert_value(row[0])
        rows.append(row)

# Write the modified data to the new output CSV file
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)  # Write the header row
    writer.writerows(rows)  # Write the modified data

print(f'Data has been successfully processed and saved to {output_file}')
