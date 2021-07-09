from slides_configuration import *

response = slides_api.delete_document_properties("test.pptx")
print(response)