from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator
import os
from pathlib import Path


RUTA_ARCHIVO = Path.joinpath(Path(__file__).parent, 'PDFs')


def procesar_archivo(nombre_archivo_nuevo: str=None):
    # url = "https://www.boletinoficial.gob.ar/pdfs/gobierno_inteligente.pdf"
    # r = requests.get(url)
    # with open('pdf.pdf', 'wb') as f:
    #     f.write(r.content)
    if not os.path.exists(RUTA_ARCHIVO):
        os.mkdir(RUTA_ARCHIVO)

    endpoints = [f for f in os.listdir(RUTA_ARCHIVO)]
    archivos = list()
    for endpoint in endpoints:
        archivos.append(str(os.path.join(RUTA_ARCHIVO, endpoint)))

    nombre_documento = max(archivos, key=os.path.getctime)
    path_doc = Path(nombre_documento)
    if nombre_archivo_nuevo is not None and (nombre_archivo_nuevo != path_doc.name):
        nombre_renombre = Path.joinpath(RUTA_ARCHIVO, nombre_archivo_nuevo)
        os.rename(nombre_documento, str(nombre_renombre))
        nombre_documento = nombre_renombre
    fp = open(nombre_documento, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed

    resource_manager = PDFResourceManager()
    laparams = LAParams()

    device = PDFPageAggregator(resource_manager, laparams=laparams)

    interpreter = PDFPageInterpreter(resource_manager, device)

    extracted_text = ""

    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)

        layout = device.get_result()

        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
    fp.close()
    print(extracted_text)
    os.chmod(RUTA_ARCHIVO, 0o777)
    os.chmod(nombre_documento, 0o777)
    return extracted_text