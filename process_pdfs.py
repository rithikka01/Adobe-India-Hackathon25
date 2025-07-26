import fitz  # PyMuPDF
import os
import json

# -------- CONFIG --------
persona = "Designer"
job_keywords = ["design", "figma", "color", "typography", "ux", "layout"]

input_folder = "input"
output_folder = "output"

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        doc = fitz.open(pdf_path)

        relevant_sections = []

        for page_num, page in enumerate(doc):
            text = page.get_text()
            for keyword in job_keywords:
                if keyword.lower() in text.lower():
                    relevant_sections.append({
                        "page": page_num + 1,
                        "matched_keyword": keyword,
                        "content": text.strip()
                    })
                    break  # only add each page once

        # Save to output
        out_filename = os.path.splitext(filename)[0] + f"_{persona.lower()}_sections.json"
        out_path = os.path.join(output_folder, out_filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(relevant_sections, f, indent=2)

        print(f"✅ Extracted relevant sections for {persona} → {out_path}")
