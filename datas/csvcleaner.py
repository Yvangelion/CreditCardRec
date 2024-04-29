import os
import csv

def process_csv(input_files, output_file, names):
    if len(input_files) != len(names):
        print("Error: Input lists must have the same length.")
        return
    
    stock_data = {name: [] for name in names}
    
    for i in range(len(input_files)):
        input_file = input_files[i]
        name = names[i]

        if not os.path.exists(input_file):
            print(f"Error: Input CSV file '{input_file}' not found.")
            continue

        with open(input_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            headers = reader.fieldnames
            if "Close" not in headers:
                print(f"Error: '{name}' column not found in the input CSV file {input_file}.")
                continue
                
            # save stocks close value 
            for row in reader:
                value = row["Close"]
                stock_data[name].append(value)

        print(f"Data from {input_file} has been processed.")

    # CSV file input
    with open(output_file, 'w', newline='') as combined_csv_file:
        writer = csv.writer(combined_csv_file)

        #headers 
        writer.writerow(names)

        # Input each stock into its own col
        for i in range(len(stock_data[names[0]])):
            row_values = [stock_data[name][i] for name in names]
            writer.writerow(row_values)

    print("CSV processing complete. Output saved to", output_file)


input_files = ["APPL.csv", "GOOG.csv", "ADBE.csv","VBMFX.csv","VTIAX.csv","VTSAX.csv","AIRXX.csv","FTDJX.csv","BND.csv"]
output_file = "combined_output.csv"
names = ["APPL", "GOOG", "ADBE","VBMFX","VTIAX","VTSAX","AIRXX","FTDJX","BND"]
process_csv(input_files, output_file, names)

