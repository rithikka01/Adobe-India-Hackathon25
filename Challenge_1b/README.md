# Adobe Hackathon - PDF Extraction Backend

## Overview
This project extracts PDF headings (Round 1A) and persona-based relevant sections (Round 1B) using Python and PyMuPDF. It’s dockerized for easy deployment.

## Features
- Extract PDF headings and outline as JSON  
- Extract relevant sections based on persona keywords  
- Runs inside Docker container for portability

## Usage
1. Place PDFs in `input/` folder  
2. Run `extract_headings.py` for full outline extraction  
3. Run `extract_relevant_sections.py` for persona-based extraction  
4. Outputs are saved in `output/` folder as JSON files

## Docker
- Build image:  
  `docker build -t adobe_pdf_extractor .`

- Run container:  

## Team
- Rithi  
- Snow

## Notes
- Requires Python 3.10+ and PyMuPDF library  
- Modify `persona` and `job_keywords` in `extract_relevant_sections.py` as needed
