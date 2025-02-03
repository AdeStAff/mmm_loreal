import pandas as pd
import os

# Define file paths
excel_file = "data/Dataset UK L'Oreal Paris Haircare - HEC Training.xlsx"
output_folder = "data/"

# Read all sheets from the Excel file
sheets = pd.read_excel(excel_file, sheet_name=None)

# Save each sheet as a separate CSV file
for sheet_name, df in sheets.items():
    csv_filename = os.path.join(output_folder, f"{sheet_name}.csv").replace(" ", "_")
    df.to_csv(csv_filename, index=False)
    print(f"Saved {csv_filename}")
