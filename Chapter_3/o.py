import fitz  # PyMuPDF

def remove_highlights(pdf_path, output_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Iterate through each annotation (highlight) on the page
        for annot in page.annots():
            if annot.type[0] == 8:  # 8 corresponds to highlight annotations
                page.delete_annot(annot)
    
    # Save the modified PDF
    pdf_document.save(output_path, deflate=True)
    pdf_document.close()

# Example usage
pdf_path = '/Users/khoale/Desktop/hands_on_ml/o.pdf'
output_path = '/Users/khoale/Desktop/hands_on_ml/output.pdf'
remove_highlights(pdf_path, output_path)
