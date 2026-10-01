import openpyxl
import pandas as pd

xlsx_file = "D:\technical-notes\Technical_References_v1.0.xlsx"
md_file = "links.md"

wb = openpyxl.load_workbook(xlsx_file)
ws = wb.active

rows = []

for row in ws.iter_rows():
    values = []
    for cell in row:
        text = str(cell.value) if cell.value is not None else ""

        if cell.hyperlink:
            url = cell.hyperlink.target
            values.append(f"{url}")
        else:
            values.append(text)

    rows.append(values)

df = pd.DataFrame(rows[1:], columns=rows[0])

with open(md_file, "w", encoding="utf-8") as f:
    f.write(df.to_markdown(index=False))

print(f"Markdown saved to {md_file}")
