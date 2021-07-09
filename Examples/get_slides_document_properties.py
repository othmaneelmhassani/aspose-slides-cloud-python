from slides_configuration import *

response = slides_api.get_document_properties("test.pptx")
print(response)