from re import template
import PyPDF2 
import sys

# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('super.pdf')

# pdf_combiner(inputs)


# with open('dummy.pdf', 'rb') as file: 
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     # print(page.rotateCounterClockwise(90))
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file: 
#         writer.write(new_file)

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermake = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermake.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file: 
        output.write(file)








