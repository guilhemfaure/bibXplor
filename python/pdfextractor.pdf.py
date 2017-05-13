import pdfx

if __name__ == '__main__':
    pdf = pdfx.PDFx("nar.pdf")
    print (pdf.get_text())
    metadata = pdf.get_metadata()
    references_list = pdf.get_references()

    print (metadata)

    for i in references_list:
        print (i)


    references_dict = pdf.get_references_as_dict()

    print (references_dict)
    #pdf.download_pdfs("here")
