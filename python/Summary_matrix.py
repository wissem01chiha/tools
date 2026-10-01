import pandas as pd
import os
import glob

# Folder containing all report files
folder_path = r"D:\MdlAdvisorReport"  # <-- change this

files = glob.glob(os.path.join(folder_path, "**", "*_ac_Report_*.xlsx"), recursive=True)


all_data = []

for file in files:
    try:
        # Extract model name from filename
        filename = os.path.basename(file)
        model_name = filename.split("_ac_Report_")[0]

        # Read Findings sheet
        df = pd.read_excel(file, sheet_name="Findings", engine="openpyxl")

        # Clean column names (handle typos/spaces)
        df.columns = [c.strip() for c in df.columns]

        # Keep relevant columns
        df = df[["Chack_Name", "Check_Status"]]

        # Add model name
        df["Model"] = model_name

        all_data.append(df)

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Combine all models
combined_df = pd.concat(all_data, ignore_index=True)

# Pivot: rows = Model, columns = Check_Name, values = Status
pivot_df = combined_df.pivot_table(
    index="Model",
    columns="Chack_Name",
    values="Check_Status",
    aggfunc="first"
)

# Optional: sort columns
pivot_df = pivot_df.sort_index(axis=1)

# Save output
output_file = "Aggregated_Report.xlsx"
pivot_df.to_excel(output_file, engine="openpyxl")

print(f" Aggregated file saved as {output_file}")