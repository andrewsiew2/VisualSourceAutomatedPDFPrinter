from PyPDF2 import PdfFileReader, PdfFileWriter
import glob

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)
        
def comparator(filename):
    return int(filename.split('\\')[1].split('_')[0])

if __name__ == '__main__':
    dirname = r'./pdfs'
    files = glob.glob(dirname + r"/*.pdf")
    files.sort(key = comparator)
    print(files)
    merge_pdfs(files, output='merged.pdf')
