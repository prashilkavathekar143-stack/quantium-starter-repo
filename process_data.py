import csv
import glob
import os

# Folder where CSV files are stored
data_folder = "data"

# Output file
output_file = "formatted_output.csv"

# List to store final rows
final_data = []

# Get all CSV files from data folder
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

for file in csv_files:
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Keep only Pink Morsels
            if row["product"] == "Pink Morsels":

                quantity = int(row["quantity"])
                price = float(row["price"].replace("$", ""))

                # Calculate Sales
                sales = quantity * price

                final_data.append({
                    "Sales": sales,
                    "Date": row["date"],
                    "Region": row["region"]
                })

# Write final formatted output
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    fieldnames = ["Sales", "Date", "Region"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(final_data)

print("✅ Data processing complete!")
print("Output file created:", output_file)
