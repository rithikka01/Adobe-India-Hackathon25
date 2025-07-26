import fitz  # PyMuPDF
import os
import json

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []

    title = os.path.basename(pdf_path).replace(".pdf", "")

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        size = span["size"]

                        if len(text) > 0 and size >= 15:
                            # Assign heading levels
                            if size > 20:
                                level = "H1"
                            elif size > 17:
                                level = "H2"
                            else:
                                level = "H3"

                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_num + 1
                            })

    return {
        "title": title,
        "outline": outline
    }

# Run for all PDFs in input/
if __name__ == "__main__":
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_headings(pdf_path)

            # Save to output JSON
            with open(os.path.join(output_dir, filename.replace(".pdf", ".json")), "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
