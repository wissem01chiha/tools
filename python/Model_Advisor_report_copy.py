import os
import shutil

# Source and destination roots
SOURCE_ROOT = r"D:\ePT_HCP_Autosar_2606A0\ePT_HCP_Autosar\STELLANTIS_Mdl"
DEST_ROOT = r"D:\MdlAdvisorReport"


def copy_mdl_advisor_reports(source_root, dest_root):
    # Ensure destination root exists
    os.makedirs(dest_root, exist_ok=True)

    found_count = 0
    missing_count = 0
    total_count = 0

    # Loop over each ring folder
    for ring_name in os.listdir(source_root):
        ring_path = os.path.join(source_root, ring_name)

        if not os.path.isdir(ring_path):
            continue

        total_count += 1

        mdl_report_path = os.path.join(ring_path, "Common", "MdlAdvisorReport")

        if os.path.isdir(mdl_report_path):
            # Direct case: Common/MdlAdvisorReport exists at ring level
            found_count += 1
            dest_ring_path = os.path.join(dest_root, ring_name)
            os.makedirs(dest_ring_path, exist_ok=True)

            print(f"[INFO] Processing {ring_name}")
            _copy_report_contents(mdl_report_path, dest_ring_path)

        else:
            # Check for multi-shot rings (sub-folders with Common/MdlAdvisorReport)
            multi_shot_found = False

            for sub_ring_name in os.listdir(ring_path):
                sub_ring_path = os.path.join(ring_path, sub_ring_name)

                if not os.path.isdir(sub_ring_path):
                    continue

                sub_mdl_report_path = os.path.join(
                    sub_ring_path, "Common", "MdlAdvisorReport"
                )

                if os.path.isdir(sub_mdl_report_path):
                    multi_shot_found = True
                    found_count += 1

                    # Destination: dest_root / sub_ring_name (flat, not nested)
                    dest_sub_ring_path = os.path.join(dest_root, sub_ring_name)
                    os.makedirs(dest_sub_ring_path, exist_ok=True)

                    print(f"[INFO] Processing multi-shot: {ring_name} -> {sub_ring_name}")
                    _copy_report_contents(sub_mdl_report_path, dest_sub_ring_path)

            if not multi_shot_found:
                print(f"[WARNING] Missing MdlAdvisorReport for: {ring_name}")
                missing_count += 1

    # Final stats
    print("\n========== SUMMARY ==========")
    print(f"Total rings scanned      : {total_count}")
    print(f"Reports found & copied   : {found_count}")
    print(f"Reports missing          : {missing_count}")
    print("Extraction completed.")


def _copy_report_contents(src_folder, dst_folder):
    """Copy all contents (files + subfolders) from src_folder to dst_folder."""
    for item in os.listdir(src_folder):
        src_item = os.path.join(src_folder, item)
        dst_item = os.path.join(dst_folder, item)

        if os.path.isdir(src_item):
            shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
        else:
            shutil.copy2(src_item, dst_item)


if __name__ == "__main__":
    copy_mdl_advisor_reports(SOURCE_ROOT, DEST_ROOT)