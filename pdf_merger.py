import sys
import PyPDF2


def merge_and_watermark(pdf_list, wtr_pdf):
    # Merge given pdfs
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")

    # Read merged pdf
    raw_pdf = PyPDF2.PdfFileReader(open("merged.pdf", "rb"))
    total_pages = raw_pdf.getNumPages()

    # Get watermark pdf
    watermark = PyPDF2.PdfFileReader(open(wtr_pdf, "rb"))
    wtr_page = watermark.getPage(0)

    # Watermark and write pages one by one
    writer = PyPDF2.PdfFileWriter()
    for page_num in range(total_pages):
        raw_page = raw_pdf.getPage(page_num)
        raw_page.mergePage(wtr_page)
        writer.addPage(raw_page)

    with open('merged_watermarked.pdf', 'wb') as output_file:
        writer.write(output_file)


if __name__ == '__main__':
    watermark_name = sys.argv[1]
    pdf_names = sys.argv[2:]

    merge_and_watermark(pdf_names, watermark_name)
