from slides_configuration import *

response = slides_api.delete_document_property("test.pptx", "author")
print(response)