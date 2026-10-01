import os
import sys
import shutil
import zipfile
from glob import glob

def create_artifact_folder_struct(ring_name, ring_full_path_2020, ring_full_path_2024):
    # Get current working directory and create base folder
    curr_path = os.getcwd()
    base_folder = os.path.join(curr_path, f"{ring_name}_ARTIFACT")
    print(f"[INFO] Creating base folder: {base_folder}")
    os.makedirs(base_folder, exist_ok=True)

    # Initialize subfolders
    subfolder_names = ['ComparisonReports', 'MigrationReports', 'R2020b', 'R2024b']
    for subfolder_name in subfolder_names:
        folder_path = os.path.join(base_folder, subfolder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"[INFO] Created subfolder: {folder_path}")

    # Copy HTML files from <ring_full_path_2024>/Report/*.html to MigrationReports
    migration_reports_folder = os.path.join(base_folder, 'MigrationReports')
    report_html_files = glob(os.path.join(ring_full_path_2024, 'Report', '*.html'))
    print(f"[INFO] Found {len(report_html_files)} HTML files to copy to MigrationReports")
    for file in report_html_files:
        shutil.copy(file, migration_reports_folder)
        print(f"[INFO] Copied HTML file: {file}")

    # Copy Production folder from 2024 to R2024b
    src_prod_2024 = os.path.join(ring_full_path_2024, 'Production')
    dest_prod_2024 = os.path.join(base_folder, 'R2024b', 'Production')
    if os.path.exists(src_prod_2024):
        print(f"[INFO] Copying Production folder from 2024: {src_prod_2024}")
        shutil.copytree(src_prod_2024, dest_prod_2024)
    else:
        print(f"[WARN] Production folder not found in 2024 path: {src_prod_2024}")

    # Copy Production folder from 2020 to R2020b
    src_prod_2020 = os.path.join(ring_full_path_2020, 'Production')
    dest_prod_2020 = os.path.join(base_folder, 'R2020b', 'Production')
    if os.path.exists(src_prod_2020):
        print(f"[INFO] Copying Production folder from 2020: {src_prod_2020}")
        shutil.copytree(src_prod_2020, dest_prod_2020)
    else:
        print(f"[WARN] Production folder not found in 2020 path: {src_prod_2020}")

    # Copy Reactis folder from 2020 to R2020b
    src_reactis_2020 = os.path.join(ring_full_path_2020, 'Reactis')
    dest_reactis_2020 = os.path.join(base_folder, 'R2020b', 'Reactis')
    if os.path.exists(src_reactis_2020):
        print(f"[INFO] Copying Reactis folder from 2020: {src_reactis_2020}")
        shutil.copytree(src_reactis_2020, dest_reactis_2020)
    else:
        print(f"[WARN] Reactis folder not found in 2020 path: {src_reactis_2020}")
        
    # Clean up any folder in the hole base_folder named with 'slprj' and delete 
    # any file with extension *.slxc file
    for root, dirs, files in os.walk(base_folder):
        # Remove 'slprj' directories
        for d in dirs:
            if d == "slprj":
                slprj_path = os.path.join(root, d)
                shutil.rmtree(slprj_path)
                print(f"[INFO] Deleted folder: {slprj_path}")
        # Remove *.slxc files
        for f in files:
            if f.endswith(".slxc"):
                file_path = os.path.join(root, f)
                os.remove(file_path)
                print(f"[INFO] Deleted file: {file_path}")
    
    
    # Copy all the contenant of the folder   ring_full_path_2024/Report/SimulationsCompare/**  
    # to base_folder/ComparisonReports
    src_folder = os.path.join(ring_full_path_2024, "Report", "SimulationsCompare")
    dest_folder = os.path.join(base_folder, "ComparisonReports")
    os.makedirs(dest_folder, exist_ok=True)
    shutil.copytree(src_folder, dest_folder, dirs_exist_ok=True)
    print(f"[INFO] Copied contents from {src_folder} to {dest_folder}")

    
    
    # Create ZIP archive
    zip_name = f"{ring_name}_ARTIFACT.zip"
    zip_path = os.path.join(curr_path, zip_name)
    print(f"[INFO] Creating ZIP archive: {zip_path}")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_folder)
                zipf.write(file_path, arcname)
                print(f"[INFO] Added to ZIP: {arcname}")
                
     # delete the base_folder
    shutil.rmtree(base_folder)
    print(f"[INFO] Deleted base folder: {base_folder}")


    print(f"[SUCCESS] Artifact ZIP created at: {zip_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python create_artifact_folder_struct.py <RingName> <RingFullPath2020> <RingFullPath2024>")
        sys.exit(1)

    ring_name = sys.argv[1]
    ring_full_path_2020 = sys.argv[2]
    ring_full_path_2024 = sys.argv[3]

    create_artifact_folder_struct(ring_name, ring_full_path_2020, ring_full_path_2024)