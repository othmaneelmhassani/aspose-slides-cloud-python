from slides_configuration import *

with open("test.pptx", 'rb') as f:
    document = f.read()

slides_api.convert_and_save(document, "PDF", "test.pdf")
