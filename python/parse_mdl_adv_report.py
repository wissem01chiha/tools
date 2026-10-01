import os
import re
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog
from openpyxl import Workbook


def parse_report(html_file):
    """Extract Run Summary from a Model Advisor report."""

    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")

    run_summary = soup.find(string=re.compile("Run Summary", re.I))
    if run_summary is None:
        return None

    table = run_summary.find_next("table")

    headers = [
        th.get_text(strip=True)
        for th in table.find_all("tr")[0].find_all("th")
    ]

    values = []
    for td in table.find_all("tr")[1].find_all("td"):
        text = td.get_text(" ", strip=True)
        m = re.search(r"(\d+)\s*$", text)
        values.append(int(m.group(1)) if m else 0)

    return dict(zip(headers, values))


def main():

    # Ask user for root folder
    root = Tk()
    root.withdraw()

    root_folder = filedialog.askdirectory(title="Select MdlAdvisorReport folder")

    if not root_folder:
        print("No folder selected.")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"

    ws.append([
        "Model",
        "Status",
        "Passed",
        "Failed",
        "Warning",
        "Information",
        "Justified",
        "Not Run"
    ])

    for model in sorted(os.listdir(root_folder)):

        model_folder = os.path.join(root_folder, model)

        if not os.path.isdir(model_folder):
            continue

        report = None

        for file in os.listdir(model_folder):
            if file.endswith("_Report.html"):
                report = os.path.join(model_folder, file)
                break

        if report is None:
            print(f"No report found for {model}")
            continue

        try:
            summary = parse_report(report)

            if summary is None:
                print(f"Cannot parse {model}")
                continue

            status = "OK" if summary["Failed"] == 0 else "NOK"

            ws.append([
                model,
                status,
                summary["Passed"],
                summary["Failed"],
                summary["Warning"],
                summary["Information"],
                summary["Justified"],
                summary["Not Run"],
            ])

            print(f"{model}: {status}")

        except Exception as e:
            print(f"{model}: ERROR ({e})")

    output = os.path.join(root_folder, "ModelAdvisor_Summary.xlsx")
    wb.save(output)

    print()
    print(f"Summary saved to:\n{output}")


if __name__ == "__main__":
    main()